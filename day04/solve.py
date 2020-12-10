import re

def part1(passports):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    print(sum(1 if all(field in passport for field in fields) else 0 for passport in passports))

def part2(passports):
    valid = 0
    for passport in passports:
        passport = passport.replace('\n', ' ')
        byr = re.match(r'.*?byr:([0-9]{4})(?: |$)', passport)
        iyr = re.match(r'.*?iyr:([0-9]{4})(?: |$)', passport)
        eyr = re.match(r'.*?eyr:([0-9]{4})(?: |$)', passport)
        hgt = re.match(r'.*?hgt:([0-9]{2,3})(cm|in)(?: |$)', passport)
        hcl = re.match(r'.*?hcl:#[0-9a-f]{6}(?: |$)', passport)
        ecl = re.match(r'.*?ecl:(amb|blu|brn|gry|grn|hzl|oth)(?: |$)', passport)
        pid = re.match(r'.*?pid:([0-9]{9})(?: |$)', passport)

        if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
            valByr = 1920 <= int(byr.group(1)) <= 2002
            valIyr = 2010 <= int(iyr.group(1)) <= 2020
            valEyr = 2020 <= int(eyr.group(1)) <= 2030
            valHgt = 150 <= int(hgt.group(1)) <= 193 if hgt.group(2) == "cm" else (59 <= int(hgt.group(1)) <= 76 if hgt.group(2) == "in" else False)
            
            if all([valByr, valIyr, valEyr, valHgt]):
                valid+= 1

    print(valid)

passports = open('day04/input.txt', 'r').read().split('\n\n')
part1(passports)
part2(passports)