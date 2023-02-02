
data = {
    'verification_method': 0,
    'verification_code': verification_code,
    'trust_this_device': 0,
    'two_factor_identifier': self.LastJson['two_factor_info']['two_factor_identifier'],
    '_csrftoken': self.LastResponse.cookies['csrftoken'],
    'username': self.username,
    'device_id': self.device_id,
    'guid': self.uuid,
}

Target >> accounts/two_factor_login/

https://www.instagram.com/explore/tags/test?igshid=YmMyMTA2M2Y=