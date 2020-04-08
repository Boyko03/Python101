import unittest
from mixins import Jsonable, Xmlable, WithSetAttributes, WithEqualAttributes
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring

class Panda(Jsonable, Xmlable, WithSetAttributes, WithEqualAttributes):
	pass

class Car(Jsonable, WithSetAttributes, WithEqualAttributes):
	pass

class NotJsonableClass(WithSetAttributes, WithEqualAttributes):
	pass

class TestJsonableMixin(unittest.TestCase):
	def test_to_json_returns_empty_json_for_objects_with_no_arguments(self):
		panda = Panda()

		result = panda.to_json(indent=4)
		expexted = {
			'type': Panda.__name__,
			'dict': {}
		}

		self.assertEqual(result, json.dumps(expexted, indent=4))

	def test_to_json_returns_correct_json_with_arguments(self):
		panda = Panda(
			name='Marto',
			age=20,
			weight=100.10,
			food=['bamboo', 'grass'],
			skills={'eat': 100, 'sleep': 200}
		)

		panda_result = panda.to_json(indent=4)
		panda_expexted = {
			'type': Panda.__name__,
			'dict': {
				'name': 'Marto',
				'age': 20,
				'weight': 100.10,
				'food': ['bamboo', 'grass'],
				'skills': {'eat': 100, 'sleep': 200}
			}
		}

		self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

	def test_to_json_returns_correct_json_with_arguments_of_jsonable_type(self):
		panda = Panda(name='Marto', friend=Panda(name='Ivo'))

		panda_result = panda.to_json(indent=4)
		panda_expexted = {
			'type': Panda.__name__,
			'dict': {
				'name': 'Marto',
				'friend': {
					'type': Panda.__name__,
					'dict': {
						'name': 'Ivo'
					}
				}
			}
		}

		self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

	def test_to_json_returns_correct_json_with_arguments_of_jsonable_type_with_arguements_of_jsonable_type(self):
		panda = Panda(name='Marto', friend=Panda(name='Ivo', friend=Panda(name='Boyko')))

		panda_result = panda.to_json(indent=4)
		panda_expexted = {
			'type': Panda.__name__,
			'dict': {
				'name': 'Marto',
				'friend': {
					'type': Panda.__name__,
					'dict': {
						'name': 'Ivo',
						'friend': {
							'type': Panda.__name__,
							'dict': {
								'name': 'Boyko'
							}
						}
					}
				}
			}
		}

		self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

	def test_to_json_raises_type_error_class_not_jsonable(self):
		panda = Panda(name='Marto', friend=NotJsonableClass(name='Ivo'))
		exc = None

		try:
			panda.to_json(indent=4)
		except Exception as e:
			exc = e

		self.assertIsNotNone(exc)
		self.assertRaises(TypeError, 'Class is not jsonable.')

	def test_from_json_with_wrong_class_type(self):
		car = Car()
		car_json = car.to_json()

		with self.assertRaises(ValueError):
			Panda.from_json(car_json)

	def test_from_json_with_no_arguments(self):
		car = Car()
		car_json = car.to_json()

		result = Car.from_json(car_json)

		self.assertEqual(car, result)

	def test_from_json_with_arguments(self):
		panda = Panda(
			name='Marto',
			age=20,
			weight=100.10,
			food=['bamboo', 'grass'],
			skills={'eat': 100, 'sleep': 200}
		)
		panda_json = panda.to_json()

		result = Panda.from_json(panda_json)

		self.assertEqual(panda, result)

class TestXmlableMixin(unittest.TestCase):
	def test_to_xml_returns_empty_xml_for_objects_with_no_arguments(self):
		panda = Panda()

		result = tostring(panda.to_xml())
		expexted = tostring(ET.fromstring('<Panda></Panda>'))

		self.assertEqual(result, expexted)

	def test_to_xml_returns_correct_xml_with_arguments(self):
		panda = Panda(name='Ivo')

		result = tostring(panda.to_xml())
		expexted = tostring(ET.fromstring('<Panda><name>Ivo</name></Panda>'))

		self.assertEqual(result, expexted)

	def test_to_xml_returns_correct_xml_with_arguments_of_xmlable_type(self):
		panda = Panda(name='Marto', friend=Panda(name='Ivo'))

		result = tostring(panda.to_xml())
		expexted = tostring(ET.fromstring('<Panda><name>Marto</name><friend><Panda><name>Ivo</name></Panda></friend></Panda>'))

		self.assertEqual(result, expexted)

if __name__ == '__main__':
	unittest.main()