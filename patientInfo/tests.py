from django.test import TestCase, Client
import json
from patientInfo.models import BaseInfo, EyeInfo, OtherInfo


class PatientInfoViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_patient_info_1(self):
        # 测试 URL
        url = '/patientInfo/post/2022-01-01-12-00-00'  # 确保日期格式正确

        # 测试数据
        data = {
            "data": {
                "id": "patient1",
                "hospital_number": "123",
                "hospital_time": "2022-01-01",
                "name": "John Doe",
                "sex": "Male",
                "age": 30,
                "nation": "USA",
                "allergy_history": "None",
                "other_allergy_history": "None",
                "eyeInfo": [
                    {
                        "eye": "Left",
                        "main_complaint": "Redness",
                        "tear_duration": 1.0,
                        "tear_accompanying_symptoms": "None",
                        "other_tear_accompanying_symptoms": "None",
                        "previous_tear_surgery": "None",
                        "other_previous_tear_surgery": "None",
                        "ocular_disease_history": "None",
                        "other_ocular_disease_history": "None",
                        "antineoplastic_drug": "None",
                        "preoperative_munk_score": 0,
                        "preoperative_discomfort_assessment": 0.0,
                        "preoperative_lacq_social_impact_score": 0.0,
                        "preoperative_gbi_score": 0.0,
                        "preoperative_appearance_score": 0.0,
                        "final_tear_duct_diagnosis": "None",
                        "dacryocystitis": "None",
                        "dacryocystitis_canaliculitis": "None",
                        "lacrimal_canaliculus": "None",
                        "nasolacrimal_duct_fracture": False,
                        "nasolacrimal_duct": "None",
                        "nasolacrimal_duct_discription": "None",  # 确保包含此字段
                        "lacrimal_punctum": "None",
                        "other_final_tear_duct_diagnosis": "None",
                        "other_final_tear_duct_diagnosis_discription": "None",
                        "other_ocular_diseases": "None",
                        "glaucoma_discription": "None",
                        "uveitis_discription": "None",
                        "diabetic_retinopathy_discription": "None",
                        "other_ocular_diseases_other_discription": "None"
                    }
                ],
                "otherInfo": {
                    "nasal_disease_history": "None",
                    "nasal_tumor": "None",
                    "nasal_septum_deviation": "None",
                    "nasal_surgery": "None",
                    "systemic_disease_and_history": "None",
                    "immune_system_disease": "None",
                    "tumor": "None",
                    "other_info": "None",
                    "nasal_endoscopy": "None",
                    "left_nasal_cavity_occupancy": "None",
                    "right_nasal_cavity_occupancy": "None",
                    "other_nasal_endoscopy_info": "None",
                    "other_body_or_systemic_disease": "None",
                    "imaging_data": "None",
                    "photos": "None",
                    "pathology_report": "None",
                    "other_special_imaging_data": "None"
                }
            }
        }

        # 发送 POST 请求
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        # 验证响应
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

    def test_add_patient_info_2(self):
        # 测试 URL
        url = '/patientInfo/post/2022-01-02-12-00-00'  # 确保日期格式正确

        # 测试数据
        data = {
            "data": {
                "id": "patient2",
                "hospital_number": "123",
                "hospital_time": "2022-01-01",
                "name": "John Doe",
                "sex": "Male",
                "age": 30,
                "nation": "USA",
                "allergy_history": "None",
                "other_allergy_history": "None",
                "eyeInfo": [
                    {
                        "eye": "Left",
                        "main_complaint": "Redness",
                        "tear_duration": 1.0,
                        "tear_accompanying_symptoms": "None",
                        "other_tear_accompanying_symptoms": "None",
                        "previous_tear_surgery": "None",
                        "other_previous_tear_surgery": "None",
                        "ocular_disease_history": "None",
                        "other_ocular_disease_history": "None",
                        "antineoplastic_drug": "None",
                        "preoperative_munk_score": 0,
                        "preoperative_discomfort_assessment": 0.0,
                        "preoperative_lacq_social_impact_score": 0.0,
                        "preoperative_gbi_score": 0.0,
                        "preoperative_appearance_score": 0.0,
                        "final_tear_duct_diagnosis": "None",
                        "dacryocystitis": "None",
                        "dacryocystitis_canaliculitis": "None",
                        "lacrimal_canaliculus": "None",
                        "nasolacrimal_duct_fracture": False,
                        "nasolacrimal_duct": "None",
                        "nasolacrimal_duct_discription": "None",  # 确保包含此字段
                        "lacrimal_punctum": "None",
                        "other_final_tear_duct_diagnosis": "None",
                        "other_final_tear_duct_diagnosis_discription": "None",
                        "other_ocular_diseases": "None",
                        "glaucoma_discription": "None",
                        "uveitis_discription": "None",
                        "diabetic_retinopathy_discription": "None",
                        "other_ocular_diseases_other_discription": "None"
                    }
                ],
                "otherInfo": {
                    "nasal_disease_history": "None",
                    "nasal_tumor": "None",
                    "nasal_septum_deviation": "None",
                    "nasal_surgery": "None",
                    "systemic_disease_and_history": "None",
                    "immune_system_disease": "None",
                    "tumor": "None",
                    "other_info": "None",
                    "nasal_endoscopy": "None",
                    "left_nasal_cavity_occupancy": "None",
                    "right_nasal_cavity_occupancy": "None",
                    "other_nasal_endoscopy_info": "None",
                    "other_body_or_systemic_disease": "None",
                    "imaging_data": "None",
                    "photos": "None",
                    "pathology_report": "None",
                    "other_special_imaging_data": "None"
                }
            }
        }

        # 发送 POST 请求
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        # 验证响应
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)


    def test_get_all_patient_info(self):
        # 先添加一个病人信息
        self.test_add_patient_info_1()
        self.test_add_patient_info_2()

        url = '/patientInfo/get/1/2'  # 根据 URL 配置修改
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)

        # 获取数据列表
        response_data = response.json()
        data_list = response_data.get('data', [])  # 确保 data 是一个列表

        # 输出列表中的所有信息
        if data_list:
            for patient in data_list:
                print("Patient Information:")
                for key, value in patient.items():
                    print(f"  {key}: {value}")
                print("-" * 40)
        else:
            self.fail("No patient data found in response")

