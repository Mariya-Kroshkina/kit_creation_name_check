import pytest
import data
import request_sender


def modify_kit_body(name):
    modified_kit_body = data.KIT_BODY.copy()
    modified_kit_body["name"] = name

    return modified_kit_body

#  Позитивные тесты
@pytest.mark.parametrize("name_positive", [pytest.param("А", id="One symbol in name"),
                                  pytest.param("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                                  bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd\
                                  abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc\
                                  dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                  cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcda\
                                  bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                                  bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                                  bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                                  bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda\
                                  bcdabcdabcdabcdabcdabcdabC", id="Acceptable number of symbols in name"),
                                  pytest.param("QWErty", id="English symbols in name"),
                                  pytest.param("Мария", id="Russian symbols in name"),
                                  pytest.param("№%@", id="Special symbols in name"),
                                  pytest.param("Человек и КО", id="Gap between symbols in name"),
                                  pytest.param("123", id="String numbers in name"),
                                  ])
def test_positive_on_name_in_kit_creation(name_positive):
    #  Arrange
    #  Act
    kit_body = modify_kit_body(name_positive)
    response = request_sender.create_kit(kit_body)
    #  Assert
    assert response.status_code == 201
    assert response.json()["name"] == name_positive


#  Негативные тесты
@pytest.mark.parametrize("name_negative", [pytest.param("", id="Fewer symbols in name than acceptable"),
                                          pytest.param("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab\
                                               cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD", id="More symbols than acceptable in name"),
                                          pytest.param("No symbols in name"),
                                          pytest.param(123)
                                          ])


def test_negative_on_name_in_kit_creation(name_negative):
    kit_body = modify_kit_body(name_negative)
    response = request_sender.create_kit(kit_body)
    assert response.status_code == 400



