import requests, lxml
from bs4 import BeautifulSoup
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}

heltermaa1 = ''
heltermaa_city = ''
number_matches = ''


def get_data():
    global heltermaa1, heltermaa_city, number_matches
    url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    result = str(soup.find_all('td'))
    pattern = re.compile(r'[A-ZÜÕÄÖ][A-Za-zÄÕÜÖöäüõ-]+')
    matches = pattern.findall(result)
    number_pattern = re.compile(r'[0-9][0-9,]+')
    number_matches = number_pattern.findall(result)


get_data()


def main():
    while True:
        user_choice = input('Please choose:\n'
                            '1.Heltermaa\n'
                            '2.Jõgeva\n'
                            '3.Jõhvi\n'
                            '4.Kihnu\n'
                            '5.Kunda\n'
                            '6.Kuressaare linn\n'
                            '7.Kuusiku\n'
                            '8.Lääne-Nigula\n'
                            '9.Narva\n'
                            '10.Pakri\n'
                            '11.Pärnu\n'
                            '12.Ristna\n'
                            '13.Roomassaare\n'
                            '14.Ruhnu\n'
                            '15.Sõrve\n'
                            '16.Tallinn-Harku\n'
                            '17.Tartu-Tõravere\n'
                            '18.Tiirikoja\n'
                            '19.Tooma\n'
                            '20.Türi\n'
                            '21.Valga\n'
                            '22.Viljandi\n'
                            '23.Vilsandi\n'
                            '24.Virtsu\n'
                            '25.Võru\n'
                            '26.Väike-Maarja\n'
                            '27.Peipsi poijaam\n'
                            '0.Exit\n')
        if user_choice == '0':
            print('Goodbye!')
            break
        elif user_choice == '1':
            print(
                f'Average temp is {number_matches[0]}. Max temp is {number_matches[1]}.'
                f' Min temp is {number_matches[2]}.'
                f' Relative humidity: average is {number_matches[3]}%, min is {number_matches[4]}%. Wind speed: average'
                f'is {number_matches[5]}m/s, max is {number_matches[6]}m/s. Rainfall is {number_matches[7]}mm.')
        elif user_choice == '2':
            print(f'Average temp is {number_matches[8]}. Max temp is {number_matches[9]}.'
                  f' Min temp is {number_matches[10]}.'
                  f' Relative humidity: average is {number_matches[11]}%, min is {number_matches[12]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[13]}m/s, max is {number_matches[14]}m/s. Rainfall is {number_matches[15]}mm.')
        elif user_choice == '3':
            print(f'Average temp is {number_matches[16]}. Max temp is {number_matches[17]}.'
                  f' Min temp is {number_matches[18]}.'
                  f' Relative humidity: average is {number_matches[19]}%, min is {number_matches[20]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[21]}m/s, max is {number_matches[22]}m/s. Rainfall is {number_matches[23]}mm.')
        elif user_choice == '4':
            print(f'Average temp is {number_matches[24]}, Max temp is {number_matches[25]}.'
                  f' Min temp is {number_matches[26]}.'
                  f' Relative humidity: average is {number_matches[27]}%, min is {number_matches[28]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[29]}m/s, max is {number_matches[30]}m/s. Rainfall is {number_matches[31]}mm.')
        elif user_choice == '5':
            print(f'Average temp is {number_matches[32]}, Max temp is {number_matches[33]}.'
                  f' Min temp is {number_matches[34]}.'
                  f' Relative humidity: average is {number_matches[35]}%, min is {number_matches[36]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[37]}m/s, max is {number_matches[38]}m/s. Rainfall is {number_matches[39]}mm.')
        elif user_choice == '6':
            print(f'Average temp is {number_matches[40]}. Max temp is {number_matches[41]}.'
                  f' Min temp is {number_matches[42]}.'
                  f' Relative humidity: average is {number_matches[43]}%, min is {number_matches[44]}%.')
        elif user_choice == '7':
            print(f'Average temp is {number_matches[45]}, Max temp is {number_matches[46]}.'
                  f' Min temp is {number_matches[47]}.'
                  f' Relative humidity: average is {number_matches[48]}%, min is {number_matches[49]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[50]}m/s, max is {number_matches[51]}m/s. Rainfall is {number_matches[52]}mm.')
        elif user_choice == '8':
            print(f'Average temp is {number_matches[53]}, Max temp is {number_matches[54]}.'
                  f' Min temp is {number_matches[55]}.'
                  f' Relative humidity: average is {number_matches[56]}%, min is {number_matches[57]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[58]}m/s, max is {number_matches[59]}m/s. Rainfall is {number_matches[60]}mm.')
        elif user_choice == '9':
            print(f'Average temp is {number_matches[61]}, Max temp is {number_matches[62]}.'
                  f' Min temp is {number_matches[63]}.'
                  f' Relative humidity: average is {number_matches[64]}%, min is {number_matches[65]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[66]}m/s, max is {number_matches[67]}m/s. Rainfall is {number_matches[68]}mm.')
        elif user_choice == '10':
            print(f'Average temp is {number_matches[69]}, Max temp is {number_matches[70]}.'
                  f' Min temp is {number_matches[71]}.'
                  f' Relative humidity: average is {number_matches[72]}%, min is {number_matches[73]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[74]}m/s, max is {number_matches[75]}m/s. Rainfall is {number_matches[76]}mm.')
        elif user_choice == '11':
            print(f'Average temp is {number_matches[77]}, Max temp is {number_matches[78]}.'
                  f' Min temp is {number_matches[79]}.'
                  f' Relative humidity: average is {number_matches[80]}%, min is {number_matches[81]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[82]}m/s, max is {number_matches[83]}m/s. Rainfall is {number_matches[84]}mm.')
        elif user_choice == '12':
            print(f'Average temp is {number_matches[85]}, Max temp is {number_matches[86]}.'
                  f' Min temp is {number_matches[87]}.'
                  f' Relative humidity: average is {number_matches[88]}%, min is {number_matches[89]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[90]}m/s, max is {number_matches[91]}m/s. Rainfall is {number_matches[92]}mm.')
        elif user_choice == '13':
            print(f'Average temp is {number_matches[93]}, Max temp is {number_matches[94]}.'
                  f' Min temp is {number_matches[95]}.'
                  f' Relative humidity: average is {number_matches[96]}%, min is {number_matches[97]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[98]}m/s, max is {number_matches[99]}m/s. Rainfall is {number_matches[100]}mm.')
        elif user_choice == '14':
            print(f'Average temp is {number_matches[101]}, Max temp is {number_matches[102]}.'
                  f' Min temp is {number_matches[103]}.'
                  f' Relative humidity: average is {number_matches[104]}%, min is {number_matches[105]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[106]}m/s, max is {number_matches[107]}m/s. Rainfall is {number_matches[108]}mm.')
        elif user_choice == '15':
            print(f'Average temp is {number_matches[109]}, Max temp is {number_matches[110]}.'
                  f' Min temp is {number_matches[111]}.'
                  f' Relative humidity: average is {number_matches[112]}%, min is {number_matches[113]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[114]}m/s, max is {number_matches[115]}m/s. Rainfall is {number_matches[116]}mm.')
        elif user_choice == '16':
            print(f'Average temp is {number_matches[117]}, Max temp is {number_matches[118]}.'
                  f' Min temp is {number_matches[119]}. Minimum surface temperature is {number_matches[120]}. '
                  f'Minimum temperature 2cm above the ground is {number_matches[121]}.'
                  f' Relative humidity: average is {number_matches[122]}%, min is {number_matches[123]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[124]}m/s, max is {number_matches[125]}m/s. Rainfall is {number_matches[126]}mm.')
        elif user_choice == '17':
            print(f'Average temp is {number_matches[127]}, Max temp is {number_matches[128]}.'
                  f' Min temp is {number_matches[129]}. Minimum surface temperature is {number_matches[130]}. '
                  f'Minimum temperature 2cm above the ground is {number_matches[131]}.'
                  f' Relative humidity: average is {number_matches[132]}%, min is {number_matches[133]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[134]}m/s, max is {number_matches[135]}m/s. Rainfall is {number_matches[136]}mm.')
        elif user_choice == '18':
            print(f'Average temp is {number_matches[137]}, Max temp is {number_matches[138]}.'
                  f' Min temp is {number_matches[139]}.'
                  f' Relative humidity: average is {number_matches[140]}%, min is {number_matches[141]}%. '
                  f'Rainfall is {number_matches[142]}mm.')
        elif user_choice == '19':
            print(f'Average temp is {number_matches[143]}, Max temp is {number_matches[144]}.'
                  f' Min temp is {number_matches[145]}. Minimum surface temperature is {number_matches[146]}.'
                  f' Relative humidity: average is {number_matches[147]}%, min is {number_matches[148]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[149]}m/s, max is {number_matches[150]}m/s. Rainfall is {number_matches[151]}mm.')
        elif user_choice == '20':
            print(f'Average temp is {number_matches[152]}, Max temp is {number_matches[153]}.'
                  f' Min temp is {number_matches[154]}.'
                  f' Relative humidity: average is {number_matches[155]}%, min is {number_matches[156]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[157]}m/s, max is {number_matches[158]}m/s. Rainfall is {number_matches[159]}mm.')
        elif user_choice == '21':
            print(f'Average temp is {number_matches[160]}, Max temp is {number_matches[161]}.'
                  f' Min temp is {number_matches[162]}.'
                  f' Relative humidity: average is {number_matches[163]}%, min is {number_matches[164]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[165]}m/s, max is {number_matches[166]}m/s. Rainfall is {number_matches[167]}mm.')
        elif user_choice == '22':
            print(f'Average temp is {number_matches[168]}, Max temp is {number_matches[169]}.'
                  f' Min temp is {number_matches[170]}.'
                  f' Relative humidity: average is {number_matches[171]}%, min is {number_matches[172]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[173]}m/s, max is {number_matches[174]}m/s. Rainfall is {number_matches[175]}mm.')
        elif user_choice == '23':
            print(f'Average temp is {number_matches[176]}, Max temp is {number_matches[177]}.'
                  f' Min temp is {number_matches[178]}. Minimum surface temperature is {number_matches[179]}.'
                  f' Relative humidity: average is {number_matches[180]}%, min is {number_matches[181]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[182]}m/s, max is {number_matches[183]}m/s. Rainfall is {number_matches[184]}mm.')
        elif user_choice == '24':
            print(f'Average temp is {number_matches[185]}, Max temp is {number_matches[186]}.'
                  f' Min temp is {number_matches[187]}.'
                  f' Relative humidity: average is {number_matches[188]}%, min is {number_matches[189]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[190]}m/s, max is {number_matches[191]}m/s. Rainfall is {number_matches[192]}mm.')
        elif user_choice == '25':
            print(f'Average temp is {number_matches[193]}, Max temp is {number_matches[194]}.'
                  f' Min temp is {number_matches[195]}.'
                  f' Relative humidity: average is {number_matches[196]}%, min is {number_matches[197]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[198]}m/s, max is {number_matches[199]}m/s. Rainfall is {number_matches[200]}mm.')
        elif user_choice == '26':
            print(f'Average temp is {number_matches[201]}, Max temp is {number_matches[202]}.'
                  f' Min temp is {number_matches[203]}.'
                  f' Relative humidity: average is {number_matches[204]}%, min is {number_matches[205]}%. Wind speed: '
                  f'average '
                  f'is {number_matches[206]}m/s, max is {number_matches[207]}m/s. Rainfall is {number_matches[208]}mm.')
        elif user_choice == '27':
            print(f'Max temp is {number_matches[209]}.'
                  f' Min temp is {number_matches[210]}.'' Wind speed: '
                  f'average is {number_matches[211]}m/s, max is {number_matches[212]}m/s.')
        else:
            print('Choice out of range!')

main()
