# Note: this NoAuth class is defined, because authorization is handled
# on API Gateway level - so we do not need to authenticate inside
# service itself


class NoAuth:
    def authenticate(self, user, passwd):
        return True

    def authorize(self):
        return True
