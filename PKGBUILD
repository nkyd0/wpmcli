# made by nkyd0 on github
pkgname=wpmcli
pkgver=1.0.0
pkgrel=1
pkgdesc="test typing speed"
arch=('any')
license=('CUSTOM')
depends=('python')

source=(
	"wpmcli.py"
	"wordlist.txt"
)

noextract=(
	"wpmcli.py"
	"wordlist.txt"
)

sha256sums=(
	'SKIP'
	'SKIP'
)

package() {
    install -Dm755 "${srcdir}/wpmcli.py" "${pkgdir}/usr/bin/wpmcli"
    install -Dm644 "${srcdir}/wordlist.txt" "${pkgdir}/usr/share/wpmcli/wordlist.txt"
}

