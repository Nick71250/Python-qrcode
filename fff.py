import qrcode


def get_qrcode(url='https://google.com', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code was created! Open {name}.png'


def main():
    print(get_qrcode(url='https://www.youtube.com/c/PyhtonToday/videos', name='youtube'))
    print(get_qrcode(url='https://instagram.com', name='instagram'))


if __name__ == '__main__':
    main()
