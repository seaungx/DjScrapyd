from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.generic.base import View
from django.shortcuts import render
from django.http import JsonResponse
from scrapyd_api import ScrapydAPI
from main.models import ScrapydItem

# Create your views here.


scrapyd = ScrapydAPI('http://localhost:6800')


        
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", locals())


class SpiderView(View):
    def get(self, request):
        task_id = request.GET.get('task', None)
        unique_id = request.GET.get('unique_id', None)

        if not task_id or not unique_id:
            return JsonResponse({"error": "Missing args"})

        status = scrapyd.job_status('default', task_id)

        if status == 'finished':
            try:
                item = ScrapydItem.objects.get(unique_id=unique_id)
                return JsonResponse({"data": item.to_dict['data']})
            except Exception as e:
                return JsonResponse({"error": str(e)})

        else:
            return JsonResponse({"status": status})

    def post(self, request):
        url = request.POST.get("url", None)

        if not url:
            return JsonResponse({"error": "Missing args."})

        if not self.is_valid(url):
            return JsonResponse({"error": "Missing args."})

        domain = urlparse(url).netloc
        unique_id = str(uuid4())

        settings = {
                "unique_id": unique_id,
                "USER_AGENT": ""
            }

        task = scrapyd.schedule('default', 'spiderMain', settings=settings, url=url, domain=domain)

        return JsonResponse({"task_id": task, "unique_id": unique_id, "status": "started"})

    def is_valid(self, url):
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            return False
        return True


