from django.shortcuts import render
import accounts.service as service


#  필요한 엔드포인트:
#  login/ : 인가코드 들고 오는 경우
#  verify/ : 토큰 들고 오는 경우(인증 및 리프레시 토큰 기반 재발급)