def hitung_momentum(massa, kecepatan) :
    momentum = massa * kecepatan
    print(f'massa = {massa / 1} Kg dengan kecepatan = {1 / 60} m/s')
    print(f'sehingga momentum = {momentum} kg m/s')
    return momentum

# massa
# kecepatan
momentum = hitung_momentum(1500, 10)

def hitung_percepatan(kecepatan, waktu) :
    percepatan = kecepatan / waktu
    print(f'kecepatan = {1 / 60} m/s dengan waktu = {waktu / 60} menit')
    print(f'sehingga percepatan = {percepatan} m/s **2')
    return percepatan

# kecepatan
# waktu
percepatan = hitung_percepatan (200, 7)


def hitung_impuls(gayaimpulsif, perubahanwaktu) :
    impuls = gayaimpulsif * perubahanwaktu
    print(f'gayaimpulsif = {gayaimpulsif / 1} Newton dengan perubahanwaktu = {perubahanwaktu / 60} menit')
    print(f'sehingga impuls = {impuls} Ns')
    return impuls

# gayaimpulsif
# perubahanwaktu
impuls = hitung_impuls (300, 7)