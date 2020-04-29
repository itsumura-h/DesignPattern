from re import match


def validateEmail(email):
    valid = 'abcdefghijklmnopqrstuvwxyz1234567890!#$%&\'*+-/=?^_`{}|~'
    if not email:
        return False
    email = email.lower()
    if email.startswith('"'):
        i = 1
        while i < min(64, len(email)):
            if email[i] in (valid + '()<>[]:;@,. '):
                i += 1
                continue
            if email[i] == '\\':
                if email[i+1:] and email[i+1] in (valid + '()<>[]:;@,.\\" '):
                    i += 2
                    continue
                return False
            if email[i] == '"':
                break
            return False
        if i == 64:
            i -= 1
        if not (email[i+1:] and email[i+1] == '@'):
            return False
        return validateDomain(email[i+2:])
    i = 0
    while i < min(64, len(email)):
        if email[i] in valid:
            i += 1
            continue
        if email[i] == '.':
            if i == 0 or not email[i+1:] or email[i+1] in '.@':
                return False
            i += 1
            continue
        if email[i] == '@':
            if i == 0:
                return False
            i -= 1
            break
        return False
    if i == 64:
        i -= 1
    if not (email[i+1:] and email[i+1] == '@'):
        return False
    return validateDomain(email[i+2:])


def validateDomain(domain):
    fqdn = r"^(?:(?:[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]{,61}[a-z0-9])\.)*(?:[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]{,61}?[a-z0-9])$"
    addr4 = r"(?:(?:[01]?[0-9]{1,2}|2(?:[0-4]?[0-9]|5[0-5]))\.){3}(?:[01]?[0-9]{1,2}|2(?:[0-4]?[0-9]|5[0-5]))$"
    if not domain or domain[255:]:
        return False
    if not domain.startswith('['):
        print(match(addr4, domain))
        print(match(fqdn, domain))
        if not (not match(addr4, domain) and bool(match(fqdn, domain))):
            print("domain 1")
            return False
        else:
            return True
    if not domain.endswith(']'):
        return False
    domain = domain[1:-1]
    if match(f"^{addr4}", domain):
        if domain != '0.0.0.0':
            return True
        else:
            return False
    if domain.endswith('::'):
        return False
    v4_flg = False
    try:
        _, last = domain.rsplit(':', 1)
    except:
        return False
    if match(addr4, last):
        if domain == '0.0.0.0':
            return False
        domain = domain.replace(last, '0:0')
        v4_flg = True
    if '::' in domain:
        oc = 8 - domain.count(':')
        if oc < 1:
            return False
        domain = domain.replace('::', f":{'0:' * oc}")
        if domain.startswith(':'):
            domain = f'0{domain}'
        if domain.endswith(':'):
            domain = f'{domain}0'
    elems = domain.split(':')
    if len(elems) != 8:
        return False
    res = 0
    for i, a in enumerate(elems):
        if a[4:]:
            return False
        try:
            print("------------")
            print(a)
            print(int(a, 16))
            res += int(a, 16) << ((7 - i) * 16)
        except Exception as e:
            return False
    return res != 0 and (not v4_flg or res >> 32 == 0xffff)


if __name__ == "__main__":
    import unittest
    valid_emails = [
        'email@domain.com',
        'firstname.lastname@domain.com',
        'email@subdomain.domain.com',
        'firstname+lastname@domain.com',
        '1234567890@domain.com',
        '_______@domain.com',
        'firstname-lastname@domain.com',
        '-email@domain',
        'abcABC123.defDEF456@ghiGHI789.comCOM012',
        "abc.#%&'/=~`*+?{}^$-|@ghi.com",
        'Abc@example.com',
        'Abc.123@example.com',
        'user+mailbox/department=shipping@example.com',
        'customer/department=shipping@example.com',
        "!#$%&'*+-/=?^_`.{|}~@example.com",
        '!def!xyz%abc@example.com',
        '"e#$$%&@>mail"@domain.com',
        '"em,ail"@localhost',
        '"Abc@def"@example.com',
        '"Fred\\ Bloggs"@example.com',
        '"Joe.\\\\Blow"@example.com',
        '"Joe.\\"Blow"@example.com',
        '".dot_kara_hazimaru"@example.com',
        '"I.likeyou."@example.com',
        '"I..love...you"@example.com',
        'email@domain-one.com',
        'email@domain.co.jp',
        'email@localhost',
        'a@a',
        'a@0.a',
        'a@a-a.com',
        'a@0-a.com',
        'a@a-0.com',
        'a@a-a.a-a',
        'email@[123.123.123.123]',
        'a@[255.255.255.255]',
        'a@[001.002.003.004]',
        'a@[2001:0db8:bd05:01d2:288a:1fc0:0001:10ee]',
        'a@[2001:db8:20:3:1000:100:20:3]',
        'a@[2001:db8::1234:0:0:9abc]',
        'a@[2001:db8::9abc]',
        'a@[::1]', 'ea@[::ffff:255.255.255.255]',
        'a@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890.com',
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/@example.com',
        '"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567+/"@example.com',
        'abcdefhghijklmnopqrstuvwxyzABC@aaaaaaaa01.aaaaaaaa02.aaaaaaaa03.aaaaaaaa04.aaaaaaaa05.aaaaaaaa06.aaaaaaaa07.aaaaaaaa08.aaaaaaaa09.aaaaaaaa10.aaaaaaaa11.aaaaaaaa12.aaaaaaaa13.aaaaaaaa14.aaaaaaaa15.aaaaaaaa16.aaaaaaaa17.aaaaaaaa18.aaaaaaaa19.aaaaaaaa20.aaaaaaaa21.aaaaaaaa22.aaaaaaaa23',
        'abcdefhghijklmnopqrstuvwxyzABCD@aaaaaaaa01.aaaaaaaa02.aaaaaaaa03.aaaaaaaa04.aaaaaaaa05.aaaaaaaa06.aaaaaaaa07.aaaaaaaa08.aaaaaaaa09.aaaaaaaa10.aaaaaaaa11.aaaaaaaa12.aaaaaaaa13.aaaaaaaa14.aaaaaaaa15.aaaaaaaa16.aaaaaaaa17.aaaaaaaa18.aaaaaaaa19.aaaaaaaa20.aaaaaaaa21.aaaaaaaa22.aaaaaaaa23.zz',
        '"abcdefhghijklmnopqrstuvwxyzABC"@aaaaaaaa01.aaaaaaaa02.aaaaaaaa03.aaaaaaaa04.aaaaaaaa05.aaaaaaaa06.aaaaaaaa07.aaaaaaaa08.aaaaaaaa09.aaaaaaaa10.aaaaaaaa11.aaaaaaaa12.aaaaaaaa13.aaaaaaaa14.aaaaaaaa15.aaaaaaaa16.aaaaaaaa17.aaaaaaaa18.aaaaaaaa19.aaaaaaaa20.com',
        '"abcdefhghijklmnopqrstuvwxyzABCD"@aaaaaaaa01.aaaaaaaa02.aaaaaaaa03.aaaaaaaa04.aaaaaaaa05.aaaaaaaa06.aaaaaaaa07.aaaaaaaa08.aaaaaaaa09.aaaaaaaa10.aaaaaaaa11.aaaaaaaa12.aaaaaaaa13.aaaaaaaa14.aaaaaaaa15.aaaaaaaa16.aaaaaaaa17.aaaaaaaa18.aaaaaaaa19.aaaaaaaa20.com'
    ]
    invalid_emails = [
        'Abc.@example.com',
        'Abc..123@example.com',
        '.dot_kara_hazimaru@example.com',
        'I.like.you.@example.com',
        'I..love...you@example.com',
        "abc.def@#%&'/=~`*+?{}^$-|.com",
        'ab<c.def@ghi.com',
        'abc.de<f@ghi.com',
        '.email@domain.com',
        'email.@domain.com',
        'email..email@domain.com',
        'あいうえお@domain.com',
        'email@-domain.com',
        'email@-.-.-.-',
        'email@123.123.123.123',
        "abc.def@ghi.#%&'/=~`*+?{}^$-|",
        'abc.def@gh<i.com',
        'abc.def@ghi.co<m',
        #
        'a@0',
        'a@0.0',
        'a@a.0',
        #
        'a@.a',
        'a@a-.a',
        'a@-a.a',
        'email@domain..com',
        'a@[::ffff:0:255.255.255.255]',
        'email@[111.222.333.44444]',
        'a@[0.0.0.0]',
        'a@[255.255.255.256]',
        'a@[example.com]',
        'a@[example.com:hoge]',
        'a@[fuga:xxxxxxx]',
        'a@[2001:0db8:bd05:01d2:288a::1fc0:0001:10ee]',
        'a@[2001:0db8:bd05:01d2:288a:1fc0:0001:10ee:11fe]',
        'a@[::]',
        'a@[0::0]',
        'a@[1::]',
        'a@[1:2:3:4:5:6:7::]',
        'a@[::255.255.255.255]',
        'a@[2001:db8:3:4::192.0.2.33]',
        'a@[64:ff9b::192.0.2.33]',
        'a@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678901.com',
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/a@example.com',
        '"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567+/a"@example.com',
        'abcdefhghijklmnopqrstuvwxyzABCD@aaaaaaaa01.aaaaaaaa02.aaaaaaaa03.aaaaaaaa04.aaaaaaaa05.aaaaaaaa06.aaaaaaaa07.aaaaaaaa08.aaaaaaaa09.aaaaaaaa10.aaaaaaaa11.aaaaaaaa12.aaaaaaaa13.aaaaaaaa14.aaaaaaaa15.aaaaaaaa16.aaaaaaaa17.aaaaaaaa18.aaaaaaaa19.aaaaaaaa20.aaaaaaaa21.aaaaaaaa22.aaaaaaaa23.zzz',
        'plainaddress',
        '@domain.com',
        'Joe Smith <email@domain.com>',
        'email.domain.com',
        'email@domain@domain.com',
        'email@domain.com (Joe Smith)',
        'email@ example',
        '"foo"."bar"@example.com'
    ]


class ValidatorTest(unittest.TestCase):
    # for e in valid_emails:
    #     locals()[f'test_valid: {e}'] = (
    #         lambda e: lambda self: self.assertTrue(validateEmail(e)))(e)
    for e in invalid_emails:
        locals()[f'test_invalid: {e}'] = (
            lambda e: lambda self: self.assertFalse(validateEmail(e)))(e)
    del e


unittest.main()
