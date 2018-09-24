from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

from essay.models import UserTicket


class UserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 校验不需要验证的地址
        not_login_path = ['/essay/login/', '/essay/register/']
        path = request.path
        for n_path in not_login_path:
            if path == n_path:
                return None
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('essay:login'))
        user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        if not user_ticket:
            return HttpResponseRedirect(reverse('essay:login'))
        request.user = user_ticket.user
