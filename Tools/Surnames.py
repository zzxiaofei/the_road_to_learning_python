mapping = {
    '0': '赵', '1': '钱', '2': '孙', '3': '李', '4': '周', '5': '吴', '6': '郑', '7': '王', '8': '冯', '9': '陈',
    'a': '褚', 'b': '卫', 'c': '蒋', 'd': '沈', 'e': '韩', 'f': '杨', 'g': '朱', 'h': '秦', 'i': '尤', 'j': '许',
    'k': '何', 'l': '吕', 'm': '施', 'n': '张', 'o': '孔', 'p': '曹', 'q': '严', 'r': '华', 's': '金', 't': '魏',
    'u': '陶', 'v': '姜', 'w': '戚', 'x': '谢', 'y': '邹', 'z': '喻', 'A': '福', 'B': '水', 'C': '窦', 'D': '章',
    'E': '云', 'F': '苏', 'G': '潘', 'H': '葛', 'I': '奚', 'J': '范', 'K': '彭', 'L': '郎', 'M': '鲁', 'N': '韦',
    'O': '昌', 'P': '马', 'Q': '苗', 'R': '凤', 'S': '花', 'T': '方', 'U': '俞', 'V': '任', 'W': '袁', 'X': '柳',
    'Y': '唐', 'Z': '罗', '.': '薛', '-': '伍', '_': '余', '+': '米', '=': '贝', '/': '姚', '?': '孟', '#': '顾',
    '%': '尹', '&': '江', '*': '钟'
}

reverse_mapping = {v: k for k, v in mapping.items()}


def surnames_decrypt(text):
    decrypted_text = ''
    i = 0
    while i < len(text):
        for length in [1, 2]:
            if text[i: i + length] in reverse_mapping:
                decrypted_text += reverse_mapping[text[i: i + length]]
                i += length
                break
        else:
            decrypted_text += text[i]
            i += 1
    return decrypted_text


if __name__ == '__main__':
    surnames = '周孙水郑孙王云郑陈福冯冯李章钱吴郑钱王王钱冯章冯云云云窦郑孙云孙水陈吴云冯陈赵苏'
    print(surnames_decrypt(surnames))
