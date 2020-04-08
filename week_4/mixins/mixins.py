import json
import xml.etree.ElementTree as ET

class WithSetAttributes:
	def __init__(self, **kwargs):
		for name, value in kwargs.items():
			setattr(self, name, value)

class WithEqualAttributes:
	def __eq__(self, other):
		return self.__dict__ == other.__dict__

class Jsonable:
	def to_json(self, indent=4):
		name = self.__class__.__name__

		attributes = self.__dict__

		attributes = Jsonable.check(attributes)

		return json.dumps({'type': name, 'dict': attributes}, indent=indent)

	@staticmethod
	def check(attributes):
		for attr in attributes:
			if '__dict__' in dir(attributes[attr]):
				if issubclass(attributes[attr].__class__, Jsonable):
					n_name = attributes[attr].__class__.__name__
					attributes[attr] = {'type': n_name, 'dict': Jsonable.check(attributes[attr].__dict__)}
				else:
					raise TypeError('Class is not jsonable.')
		return attributes

	@classmethod
	def from_json(cls, json_string):
		data = json.loads(json_string)

		class_name = data['type']

		if class_name != cls.__name__:
			raise ValueError('Wrong type.')

		attributes = data['dict']

		return cls(**attributes)

class Xmlable:
	def to_xml(self):
		root = ET.fromstring(f'<{self.__class__.__name__}></{self.__class__.__name__}>')

		if self.__dict__ == {}:
			return root

		attributes = self.__dict__
		attributes = Xmlable.to_dict(attributes)

		root = Xmlable.prepare(root, attributes)
		return root

	@staticmethod
	def to_dict(attributes):
		for attr in attributes:
			if '__dict__' in dir(attributes[attr]):
				if issubclass(attributes[attr].__class__, Jsonable):
					attributes[attr] = Xmlable.to_dict(attributes[attr].__dict__)

		return attributes

	@staticmethod
	def prepare(root, attributes):
		for attr in attributes:
			root.append(ET.fromstring(f'<{attr}>{Xmlable.prepare(root.tag, attributes[attr])}</{attr}>'))

		return root

	def from_xml(self):
		pass

if __name__ == '__main__':
	main()