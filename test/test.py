import logging

if __name__ in ("__main__", "test"):
    # 파일을 이용하는 것은 아님. 만약 제대로 사용하려면 상대 경로로 실행해야 함.
    logging.warning('파일이 아닌 설치된 모듈에서 실행되고 있습니다.')
    import requests_utils
else:
    from .. import requests_utils


if __name__ == "__main__":
    pass
