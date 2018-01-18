import requests

class Paloalto_api(object):
    """docstring for paloalto_api."""
    XPATH = "/config/devices/entry[@name='localhost.localdomain']" + \
            "/vsys/entry[@name='vsys1']"
    
    def __init__(self, url, api_key, proxies={}):
        self.url = url
        self.api_key = api_key
        self.proxies = proxies
        self.https_verify = True
    
    def set_proxy(self, proxy):
        """Establecer proxy para la comunicación"""
        self.proxies = proxy
    
    def set_https_verify(self, https_verify):
        """Verificar certificado HTTPS"""
        self.https_verify = https_verify
    
    def commit(self):
        """Commit"""
        data = {
            'type': 'commit',
            'cmd': '<commit/>'
        }
        return self._navegador(data)
    
    def get_config(self):
        """Retorna un XML con la configuration actual"""
        data = {
            'type': 'export',
            'category': 'configuration',
        }
        return self._navegador(data)
    
    def get_address(self, address):
        """Retorna un xml del relacionado con el nombre pasado"""
        data = {
            'type': 'config',
            'action': 'get',
            'xpath': self.XPATH + "/address/entry[@name='%s']" % address
        }
        return self._navegador(data)
    
    def create_address(self, nombre, ip, descripcion):
        """ Crea un objeo de tipo dirección en PaloAlto"""
        data = {
            'type': 'config',
            'action': 'set',
            'xpath': self.XPATH + "/address/entry[@name='%s']" % nombre,
            'element': "<ip-netmask>%s</ip-netmask>" % ip + \
                "<description>%s</description>" % descripcion
        }
        return self._navegador(data)
    
    def delete_address(self,nombre):
        """Elimina la dirección relacionada con el nombre pasado"""
        data = {
            'type': 'config',
            'action': 'delete',
            'xpath': self.XPATH + "/address/entry[@name='%s']" % nombre
        }
        return self._navegador(data)
    
    def create_rule(self,  *args, **kwargs):
        """Crear regla en FW"""
        # TODO: jinja2
        return False
    
    def delete_rule(self, rule):
        """Eliminar regla de seguridad"""
        data = {
            'type': 'config',
            'action': 'delete',
            'xpath': self.XPATH + "/address/entry[@name='%s']" % nombre
        }
        return self._navegador(data)
    
    def add_group_address(self, group, address):
        """Añade una dirección a un grupo y crea el grupo si no existe"""
        data = {
            'type': 'config',
            'action': 'set',
            'xpath': self.XPATH + "/address-group/" + \
                "entry[@name='%s']/static" % group,
            'element': '<member>%s</member>' % address
        }
        return self._navegador(data)
    
    def delete_group_address(self, group, address):
        """ Eliminar dirección de un grupo"""
        data = {
            'type': 'config',
            'action': 'delete',
            'xpath': self.XPATH + "/address-group" + \
                "/entry[@name='%s']/static" % group + \
                "/member[text()='%s']" % address
        }
        return self._navegador(data)
    
    def delete_group(self, group):
        """Eliminar grupo de direcciones"""
        data = {
            'type': 'config',
            'action': 'delete',
            'xpath': self.XPATH + "/address-group" + \
                "/entry[@name='%s']" % group
        }
        return self._navegador(data)
    
    def _navegador(self, data):
        data.update({'key': self.api_key})
        return requests.get(
            self.url,
            data,
            proxies=self.proxies,
            verify=self.https_verify
        ).content


def get_api_key(url, user, password):
    """Retorna API_KEY"""
    return requests.get(url, {
        'type': 'keygen',
        'user': user,
        'password': password
        },proxies=proxies, verify=False
    ).content
