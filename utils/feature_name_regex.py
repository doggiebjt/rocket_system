import os
import re
from pypinyin import lazy_pinyin


def get_text_prefix(text):
    text_pinyin = lazy_pinyin(text)
    return "".join([_[0] for _ in text_pinyin])


def feature_regex_match(feature_names, regex_rule):
    feature_names_dict = dict()
    for feature_name in feature_names:
        result = re.findall(regex_rule, feature_name)
        assert len(result) == 1, "feature_regex_match error: {}".format(feature_name)
        suffix = result[0]
        # feature_name_new = feature_name.strip(suffix)  # unknown error
        feature_name_new = feature_name[:-len(suffix)]
        feature_name_new = feature_name_new.replace("（", "").replace("）", "").replace("°", "度"). \
            replace("一级", "1级").replace("二级", "2级").replace("三级", "3级")

        abbr = get_text_prefix(feature_name_new)
        feature_names_dict[feature_name] = (feature_name_new, suffix, abbr)
    return feature_names_dict


if __name__ == '__main__':
    feature_names = ['星箭分离面切向高频振动1V8xjflmqg01']
    regex_rule = "V[a-zA-Z0-9]+[0-9]$"
    feature_names_dict = feature_regex_match(feature_names, regex_rule)
    print(feature_names_dict)
