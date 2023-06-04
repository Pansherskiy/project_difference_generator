import pytest
import os


@pytest.fixture
def json_file1():
    tmp_file_path = "test_file1.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def json_file2():
    tmp_file_path = "test_file2.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def empty_json_file():
    tmp_file_path = "test_file3.json"
    file = open(tmp_file_path, 'w')
    file.write('{}')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def empty_file():
    tmp_file_path = "test_file4.json"
    file = open(tmp_file_path, 'w')
    file.write('''''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def nested_json_file1():
    tmp_file_path = "test_file5.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": true,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def nested_json_file2():
    tmp_file_path = "test_file6.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def simple_json_result1():
    return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


@pytest.fixture
def simple_json_result2():
    return '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''


@pytest.fixture
def simple_json_result3():
    return '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''


@pytest.fixture
def simple_json_result4():
    return '''{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50
}'''


@pytest.fixture
def nested_json_result1():
    return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


@pytest.fixture
def nested_json_result2():
    return '''{
    common: {
      - follow: false
        setting1: Value 1
      + setting2: 200
      - setting3: null
      + setting3: true
      - setting4: blah blah
      - setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: so much
              + wow: 
            }
            key: value
          - ops: vops
        }
    }
    group1: {
      - baz: bars
      + baz: bas
        foo: bar
      - nest: str
      + nest: {
            key: value
        }
    }
  + group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  - group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


@pytest.fixture
def nested_json_result3():
    return '''{
  - common: {
        follow: false
        setting1: Value 1
        setting3: null
        setting4: blah blah
        setting5: {
            key5: value5
        }
        setting6: {
            key: value
            ops: vops
            doge: {
                wow: so much
            }
        }
    }
  - group1: {
        foo: bar
        baz: bars
        nest: str
    }
  - group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
