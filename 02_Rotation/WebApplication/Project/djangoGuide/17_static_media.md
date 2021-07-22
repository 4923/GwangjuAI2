`settings.py`

> 이미지 파일을 문제없이 업로드 하기 위함

**STATIC_ROOT를 추가한다.**
- staticfiles를 모아두는 root dir

```py
# STATIC_URL = '/static/'   # 기존의 값

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

**MEDIA_URL, MEDIA_ROOT를 추가한다.**
- 이미지 등을 모아두는 공간

```py

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```