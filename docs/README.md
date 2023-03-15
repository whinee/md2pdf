<h1 align="center" style="font-weight: bold">
    md2pdf
</h1>

<!-- Description. Preferably 1 sentence long. -->
<h2 align="center" style="font-weight: bold">
    Markdown to PDF converter
</h2>

<p align="center">
    <a href="https://github.com/whinee/md2pdf/issues">
        <img src="https://img.shields.io/github/issues/whinee/md2pdf.svg?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAABmJLR0QA/wD/AP+gvaeTAAACVUlEQVR4nO3doW5UQRTG8XPaEHwLBgQhCGoQJLwAiiYY3qCG10DgCc/QJ0AgMCTUIkCCqiAhkCBQpNAW0g+xS5pguLv3DPeb3f/P35OZ+XJm7+yIGwEAAAAAALAQSW813pup5zHExtQDGOi0oMZJQY3megmkYjEJpBCBmCEQMwRihkDMVCzmcUGN5tYpEDqkEOcQM3SIGQIxQyBmCMQMgZghEDMVr70cDAvRIWYIxAyBmCEQMwRihkDMEIgZLqjMcB9ihi3LDIGYIRAzYxfzLDN/loyksS4CyczTiNCIEhUvBf9FF4HMjVnULl55I/oKZMy21cXvRwSB2OkpkDFbFoE0QIeYIRAzBGKGQMyMWVTOIQ3QIWYIxAyBmOFgaIYOMUMgZgjEDIGY4WBohg4xw2uvGTrEzFoEklMPYChJ1yPizpKPv87Mj5XjAQAAAACgiW5O6n+bn9zvRsStiNiK2Vy+RsT7iDjIzMMJh7c+JN2W9ELS2T++F/JS0rJ/tWAISXuSjhf4iMuJpIdTj3slSdqV9Gvh7+rMnrk/9fhXiqQLkg6XCOOPD5IuTj2PIXq5D3kQETdGPH9tXsNeL4HsFtS4V1CjuV4C2SmocbOgRnO9BLJVUONSQY3megnkqKDGt4IazfUSyCeTGs31EsirghoHBTUQESHpiqTvI84hPyRdnXoeQ3TRIZn5OSKejCjxNDO72LK6IWlT0rMluuO5pM2px7+SJG1IeiTpaOA29bi3MLq8D5F0OSL24vw+ZDvO70PexewHfD8zv0w2SAAAAAAAsAJ+A9PfbN9hclgfAAAAAElFTkSuQmCC">
    </a>
    <a href="https://github.com/whinee/md2pdf/network/members">
        <img src="https://img.shields.io/github/forks/whinee/md2pdf.svg?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAABmJLR0QA/wD/AP+gvaeTAAAFKElEQVR4nO2dS4gcRRjH/xXdoKiIaESNio8YCbKKRgSJ4knEg8km0eArQUTwZIJXL8GTWYMoehC8xgfRgxvjUfAg+IoPsi5Bze76TiIo4jqCu5vMz0NNS+zMzM5OV+9X3VM/GHabXb761/zpenzdVSUlEolEIpFIJMLjyggKLJc00vrcJOnS1p9+lvSFpDFJY865uTLKT5wEsAmYYmEmgY3WemsLsAx4tgcj8owCy6z11w5gdx9mZOyy1l8r8M1UUUas61ELgOX4/qAoU/jBwEATou0ekXR1gDhXSVofIE6lCWFIyJHSwDdbIQxZGyBGxs0BY1WSEIZcHCBGxsqAsSrJ6QFilDLbt4QqZxrobVbeK4cjqE+1Mw3AawEN2WNYj3pkGoD7AxqyxbAe/ZiRMWql+xSAIeD7AGZMAyH6tH7qUK9MA7A+QIU2GWmvZ6YBeL5AZZ4z1L0lgBkZ91rV4xQAB7zQjxmA2dAZeD2gIa9a1aMj+Pb4ux7ETxNBuwt8E9CQr63r0xZ8R/8gsLeN6L3AA8CQtU5JAmYCGjJTVE/pTQXA/wp0LqqZPdCQdFagcA3n3DlFAsQzobHjWEyxkiHSpwFjfVw0QDJEeidgrP1FA6Q+xA8uJiVdXjDUtKRrnXPHiwQZ+DvEOTcv6YkAoXYUNWNJyI8LrfV0gv4mtRm7rfX3TIUMccCLizSiic8SR9UMd6UqhmTgc1s/9GDGJHCPtd5FUzVDpP8ywFuBsZz8efwDufswelRQmCoakgGsyt8VZZc58KOsBbgsd/1L2QUmQ7qTfyPzaNkFJkO6c0vuerzsApMh3bk9dx0y72VDVTt1YDgnfQ44t+xy0x3SmUdz1+855/40URKSKt4hwIXA3znp26x1BaGihuTfxjwKnGmtKwhVMwQ/Q8/zpLWuYFTJEOAuYDYneQI4w1pbMKpiCPBYGzPmgJALkuyJ3RDgIuCtNs1UE9hqrS84sRoCrMQvJWi0MeMEsN1aYynEZAiwAngEn1afb2ME+OHuZkudpWJpCHA+cDewE/gAON7BhIwPgdVLqTFPNR+y5MCvYLpS0vWSrpM0LOlGSdf0GOJHSTsl7XHOnShFZI9UzhDgPPkvfrj18wZ5E/p5HfSApJckvemcmw0msgDRGwKskXSHpNskrZN0RYFwTUkfya+ifds5N1VcYViiNAS4VdJmSRskrSoQalbSl/KveH4i6X3n3K/FFZZHNIYAZ0vaJulx+aZosRyT9JWkidZnXNJ4lGvJu2BuCHCafKr7afW2K8SspIPyC/jHJR2SNOGc+700kXWi27AXWAMcXGAo2gDeBbYDa4lkoU9l6WQI8BDwVwcT/gHeAO4kppWtdaCdIcCODkbMAE8BK6x115Y2X/rD+FxRnv1A0SUBiYVo88Xnc0gNjDYNGEg6NE0nm7HOWuNA0cWMJhGsUx84uhjysrW2gaSDGX8AF1hrixGrF+Vecc79ZlT2YNPhDun1OUUiNG3MOGStKWaWIrm4WtKR1u+XLEF5iUQikVga0hlUdYeq7wxdF6jLztB1gXQGVTxQt52hqwx13RnaiHQGVWSkM6giI51BFRnpDKrIiG3837QWYE0IQ44s/C8msSpJCEM+CxAj40DAWJUkhCH7AsTICLnL9GCCP5ricJoYRgSwsaAZTWDgJ4VBodixc89Y668d+PT7aB93xi5S+r08gBF661O+BTZY642Nsh7hDsmvoB2RT61kj3B/kvS5/MhsX+tkgkQikUgkEolEomT+BQYopfF8o1GKAAAAAElFTkSuQmCC">
    </a>
    <a href="https://github.com/whinee/md2pdf/stargazers">
        <img src="https://img.shields.io/github/stars/whinee/md2pdf.svg?style=for-the-badge&logo=data:image/png;base64,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">
    </a>
    <a href="https://github.com/whinee/md2pdf/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/whinee/md2pdf.svg?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAABmJLR0QA/wD/AP+gvaeTAAAF4UlEQVR4nO3cW4hVVRzH8d+acSrNSUXzAl28JlaiXTQqoaxeBJlIsiDsoRfJJJJIQnsou0APUWCRPRp2eQgLL6BYkQQh4QUtNXRGorLMGctb3p359rDOyDicmb332Wudy/j/PJ45+7//a//POnvttdYZyRhjjDHGGGOMMcYYY4wxxhhjjDHFuEon0AkYJuk6Sf84545XOp8rCtAAPAIsB/YDZ7ncKWAn8BYwDaiaD06fAjhgLtBCNj8Dsyudf58CjAO2ZyxEd2uBIZVuS80DZgCHcxajUzMwqdJtqlnATOB8oGJ0agPGVrptNQcYA7QGLkanvcCgSrexZgB15L9nJFlZ6XbWDODpyMUAaAfurHRbQ4oyvgcaJO2XNDpG/G42OudmhQoG1EmaLqlJ0m2SRkhql/S3pG2S1jjn9oY6X1kAD5ehd3TtJSMD5T0L2JXinF9TSz0TeD9mBYqYnzPfeuDtjOe8CLwc6ppFhZ8OKaevcuRaB6zOce7XQ1674PDTI93npmJrzpHvGznP3QE8Eer6Bb+p42dt20LHTfCfc64x60HALZJ2S2rIef5WSROccydyxlFd3gBFDI4QM0n/Eo97VfmLIUnDJS0MECdKDxkk6VjouAmOO+cyfRCA/vI9+dpAOexyzk3NGyR4DyksLp0OHTfBwRKOmaHkYpyQ9JGkVZIuJLx3CjCqhDwu0y9vgB40S5oSKXYxO0s45uaEv3dImumc2yFJwCb5wvRmtKRDJeRySYx7iCStjxQ35PmuT/j7wc5iFKwJEDNRrIKsjRS3mPOSNpRw3NGEv48CuvaiewPETBTrK2urpO2S7ooUv6vPS9wUkXTfaZD0LfCepEZJL6WI+UcJeVwm2uYB4EFJ38WKX3BW0kTn3O9ZDyyMBlslXRUolwPOufF5g8T6ypJzbrOkdbHiF7xTSjGkS6PBbwLmsjpgrDiA64A9OacmerIJyPWVC0wvTH3kdZJAM87RARPxa+Ah7QGCzAgAKwPk82KIXMoGGAvsDtBwgI0EKkYht/7Ajzny+ZRa3MgHNOI/je0lNvwMfma2PkJugwuFzupD/Opo7QKmAhsyFOYcvpA3Rc6rHlgEHEmR0wECTrl3VbGuhr8JNkmaJel2+bXrRvmJyYOSfpJ/wNxYzs3X+OHwnEJut0q6QX4e60/5Z6s1ktY5586XKydjjDEmjbLe1IGr5ddJJkgaL2mcpCHyS7CdzxYdkjoXudoktUg6IGmfpD3OufaI+Q2XdL/8pOg4SSPlBxqSdE7SSUm/SdoraYekLc65i7HyiaIwzF0GbAZOpx/iF3UMWA8sBsYEym8g8BzwA9mnUY7iHwwfCJFLNMAw4BXgl5wF6E0HsAVYAAwoIcdrgCXAv4Hy2QY8FON6lgy4EVhB/p6QVRu+F6b6eQIwBdgXKZdVafOIBhhQuCCnIjUyrcPAfHqZXgGewU/DxNQCTCxnDbo28B7Kv3U0yff0cI8BZuP35cZ2BMi9LShrMRYDF8rQuFIcBx7rIe+FZcqhlUCDj6RC9CPMOkJsHcDSHtrwbply2Iof7qeS+TkE//38maQos52RvOacW9b1BfwPc76U9GiR95+R36jRLOlI4bVGSUMlTZY0Sdmu3XLn3AtZk06En6L+pEyfrNCWFGnPIPzPrDu1AE/ht5n2dh2G4p9d0g7r24lxP8EPaWvZs0XaNA1/k/8YGJjxejQAS0k3SAi5oUIC5kW7TOVzFri7SNuayLEMCzxOugW3xF6SKgn8mHqbpEyfoCr1q6Q7ui96AU2SUt98i1gk6b6E93zgnHu+tzek3UazQn2jGJI0RtKbkrpfmHmS5kY+94ikNyRulAOelDQzSDrVYwEwudtraTZTR5dm5+Kc6FmUX72k7g+NVbFGnqYgtbfnKJ1o22jzqMqkrmRWkCpjBakyVpAqE+sXVDXHOfeFqmAAYz2kylhBqowVpMokfmfi//tnX/xfuYecc39VOgljjDHGGGOMMcYYY4wxxhhjjDHGpPM/BWpSvDWwvc0AAAAASUVORK5CYII=">
    </a>
    <a href="https://m2p.whinyaan.xyz/license.html">
        <img src="https://img.shields.io/badge/LICENSE-A31F34?style=for-the-badge&logoWidth=25&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANwAAAByCAYAAAA4TL8fAAADvElEQVR4nO3bsYkdVxiG4c2EA6kCY5WgAt2AMuVbgntRC+rgcoeFTRbDcQ3/OxwxjJ8P/vTwBvOE8/J8PteuO47j35cTO47jubNvrfX5RNuvzW1/nWj7ubPt4+PjW21ba33Z2Xb1e9n5OHCn2oC74QHX24ALA27j48CdagPuhgdcbwMuDLiNjwN3qg24Gx5wvQ24MOA2Pg7cqTbgbnjA9TbgwoDb+Dhwp9qAu+EB19uACwNu4+PAnWoD7oYHXG8DLgy4jY8Dd6oNuBsecL0NuDDgNj4O3Kk24G54wPU24MKA2/g4cKfagLvhAdfbgAsDbuPjwJ1qA+6GB1xvAy4MuI2PA3eqDbgbHnC97bLg3t7evr+/v/+z69ZaX2vbWuuPnW1XP+B622XB2YUHXG4DzuYDLrcBZ/MBl9uAs/mAy23A2XzA5TbgbD7gchtwNh9wuQ04mw+43AaczQdcbgPO5gMutwFn8wGX24Cz+YDLbcDZfMDltsuCW2v9vdZ63Xh/nmj7dBzH6657PB4/attvGXC57crgfq69O/M/3OfN39yztv2WAZfbgGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AAZfagGttwAGX2oBrbcABl9qAa23AXRXc4/H4cRzH665ba32qbcDlNuCuCu7KAy63AQfcfMDlNuCAmw+43AYccPMBl9uAA24+4HIbcMDNB1xuAw64+YDLbcABNx9wuQ044OYDLrcBB9x8wOU24ICbD7jcBhxw8wGX24ADbj7gchtwwM0HXG4DDrj5gMttwAE3H3C5DTjg5gMutwEH3HzA5TbggJsPuNwGHHDzAZfbgANuPuByG3DAzQdcbgMOuPmAy23AATcfcLkNOODmAy63AQfcfMDlNuCAmw+43AYccPMBl9uAA24+4HIbcMDNB1xuAw64+YDLbcABNx9wuQ044OYDLrcBB9x8wOU24ICbD7jcBhxw8wGX2/7X4P4DxDPxnlw4RDoAAAAASUVORK5CYII=">
    </a>
</p>
<p align="center">
    <a href="https://wakatime.com/badge/user/c355e5b6-46c1-4616-be40-bffc807ffbb8/project/c7ba73de-30be-46ad-a260-bd2dca7d591c">
        <img alt="wakatime" src="https://wakatime.com/badge/user/c355e5b6-46c1-4616-be40-bffc807ffbb8/project/c7ba73de-30be-46ad-a260-bd2dca7d591c.svg?style=for-the-badge">
    </a>
    <a href="https://app.codacy.com/gh/whinee/md2pdf/dashboard">
        <img alt="Codacy Badge" src="https://img.shields.io/codacy/grade/ad76078b89514f75ba385a19efe19941?style=for-the-badge">
    </a>
    <a href="https://github.com/whinee/md2pdf/releases">
        <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/whinee/md2pdf?include_prereleases&style=for-the-badge">
    </a>
    <a href="https://github.com/whinee/md2pdf/releases">
        <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/whinee/md2pdf/test.yml?branch=main&label=Build&style=for-the-badge">
    </a>
</p>
<p align="center">
    <a target="_blank" href="https://discord.com/invite/JbAtUxGcJZ">
        <img src="https://invidget.switchblade.xyz/JbAtUxGcJZ">
    </a>
</p>

---

<!-- Motto section. Preferably 2-5 sentences long. -->
<h4 align="center">
For writing faster? No. For writing with *class*? Yusss
</h4>

---

Github: [github.com/whinee/md2pdf](https://github.com/whinee/md2pdf)

Website: [m2p.whinyaan.xyz](https://m2p.whinyaan.xyz)

---

To be updated, be sure to watch this repository and join the [Discord Support Server](https://discord.com/invite/JbAtUxGcJZ) for this and other projects.

Interested in commissioning projects? Inquire through Discord(<a target="_blank" href="https://discord.com/users/848092597822160907">whi_ne#4783</a>) or through e-mail(<a target="_blank" href="mailto:whinyaan@protonmail.com">whinyaan@protonmail.com</a>). Price starts at 30 USD.


<div class="toc"><h2 id="toc"><b><a href="#toc">Table of Contents</a></b></h2>
<ul><li><a href="#important">Important</a></li><li><a href="#downloads">Downloads</a></li><li><a href="#what-s-this">What’s this?</a><ul><li><a href="#what-s-this-supported-oses">Supported OSes</a></li></ul></li><li><a href="#usage">Usage</a></li><li><a href="#getting-started">Getting Started</a></li><li><a href="#advantages">Advantages</a></li><li><a href="#disadvantages">Disadvantages</a></li><li><a href="#translations">Translations</a></li><li><a href="#known-issues-and-limitations">Known Issues and Limitations</a></li><li><a href="#considerations">Considerations</a></li><li><a href="#contributions">Contributions</a></li><li><a href="#license">License</a><ul><li><a href="#license-mit">MIT</a></li></ul></li><li><a href="#attribution">Attribution</a><ul><li><a href="#attribution-mit-logo">MIT Logo</a></li><li><a href="#attribution-icons">Icons</a></li></ul></li><li><a href="#further-reading">Further Reading</a></li></ul></div>

<h2 id="important"><b><a href="#important">Important</a></b></h2>

md2pdf is still in Unreleased Alpha Development Stage.

Using the program at this stage is not recommended.

<h2 id="downloads"><b><a href="#downloads">Downloads</a></b></h2>

Since people are looking for the download first, here you go:

Follow [this link](docs/0/0/installation.md) to install md2pdf in your machine.

<h2 id="what-s-this"><b><a href="#what-s-this">What’s this?</a></b></h2>

md2pdf is a [Markdown](docs/0/0/markdown.md) to PDF converter that can also do a lot of stuff:

- Headers and Footers
    - Can be in Markdown or HTML format
    - Support for first page header and footer
- Print output HTML
- Programmatic Usage

<h2 id="what-s-this-supported-oses"><b><i><a href="#what-s-this-supported-oses">Supported OSes</a></i></b></h2>

- Windows
- MacOS
- Linux

<!-- Mention examples of application of this repository. -->
<h2 id="usage"><b><a href="#usage">Usage</a></b></h2>

<i><font color="#ED5E5E">
    This section is not yet complete.
</font></i>

<h2 id="getting-started"><b><a href="#getting-started">Getting Started</a></b></h2>

Visit [this link](docs/0/0/getting-started) to get started. The instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h2 id="advantages"><b><a href="#advantages">Advantages</a></b></h2>

- Standardized Styles
- Consistent Results
- Programmatic Usage

<h2 id="disadvantages"><b><a href="#disadvantages">Disadvantages</a></b></h2>

- This program does not guarantee that you will be able to write faster, just be able to write in markdown (effectively plaintext) and produce consistent results (assuming that you use the same text, settings, stylesheet/s, and whatnot)
- Have to link pictures online in order to attach one in the document, unlike in fancy word editors like Microsoft Word or LibreOffice Writer

<h2 id="translations"><b><a href="#translations">Translations</a></b></h2>

This program is translation ([i18n](https://en.wikipedia.org/wiki/Internationalization_and_localization#Naming)) ready!

Please refer to [this link](docs/0/0/contribute/translations.md) to learn more on how to create a translation for this program.

<!-- Mention the issus and limitations of this repository. Preferably 1-5 sentences long. -->
<h2 id="known-issues-and-limitations"><b><a href="#known-issues-and-limitations">Known Issues and Limitations</a></b></h2>

- This program can not be run in termux due to an inherent bug in AOSP that the said org's developers refuses to fix even if it will only take (apparently) a change in a single line of code (I forgot where the relevant Stackoverflow link is stored at, nor do I know the keywords for searching it up)

<h2 id="considerations"><b><a href="#considerations">Considerations</a></b></h2>

I want to implement more features as to extend the markdown specification, and in [this link](considerations.md), you can see the following considerations to be made for future feature implementations.

If you want to help, check the [TODO](TODO.md) of the developer and the [contribution guidelines](contributing.md).

<h2 id="contributions"><b><a href="#contributions">Contributions</a></b></h2>

For the contribution guidelines, visit [this link](contributing.md).

For contributing in the latest version of md2pdf, visit [this link](docs/0/0/contribute/index.md)

<!-- License section. Leave unchanged except when changing the style altogether. -->
<h2 id="license"><b><a href="#license">License</a></b></h2>

### <a target="_blank" href="https://choosealicense.com/licenses/mit/">MIT</a>

Copyright for portions of project <a target=_blank
href="https://github.com/whinee/md2pdf">md2pdf</a> are held by [Julien Maupetit, Github account <a target=_blank
href="https://github.com/jmaupetit">jmaupetit</a> owner, 2016-2021] as part of project
<a target=_blank href="https://github.com/jmaupetit/md2pdf">md2pdf</a>, by [c4ffein, Github account <a target=_blank
href="https://github.com/c4ffein">c4ffein</a> owner, 2021-2022] as part of project
<a target=_blank href="https://github.com/c4ffein/txt2pdf">txt2pdf</a>, by [Simon Sapin, Github account <a target=_blank
href="https://github.com/SimonSapin">SimonSapin</a> owner, 2011-2023] as part of project
<a target=_blank href="https://github.com/Kozea/WeasyPrint">WeasyPrint</a>, by [Pallets, Github account <a target=_blank
href="https://github.com/pallets">pallets</a> owner, 2014-2022] as part of project
<a target=_blank href="https://github.com/pallets/click">click</a>, by [mbarkhau, Github account <a target=_blank
href="https://github.com/mbarkhau">mbarkhau</a> owner, 2019-2021] as part of project
<a target=_blank href="https://github.com/mbarkhau/markdown-katex">markdown-katex</a>, by [Python-Markdown, Github account <a target=_blank
href="https://github.com/Python-Markdown">Python-Markdown</a> owner, 2007-2023] as part of project
<a target=_blank href="https://github.com/Python-Markdown/markdown">markdown</a>, by [whi_ne, Github account <a target=_blank
href="https://github.com/whinee">whinee</a> owner, 2021-2022] as part of project
<a target=_blank href="https://github.com/MangDL/MangDL">MangDL</a>, and by [whi_ne, Github account <a target=_blank
href="https://github.com/whinee">whinee</a> owner, 2022] as part of project
<a target=_blank href="https://github.com/Pirate-Kings/YAMHL">YAMHL</a>.

All other copyright for project <a target=_blank
href="https://github.com/whinee/md2pdf">md2pdf</a> are held by [Github
Account <a target=_blank href="https://github.com/whinee">whinee</a> Owner, 2023].

Check the [LICENSE](LICENSE.md) for more details.

<h2 id="attribution"><b><a href="#attribution">Attribution</a></b></h2>

<h2 id="attribution-mit-logo"><b><i><a href="#attribution-mit-logo">MIT Logo</a></i></b></h2>

<a target="_blank" href="https://commons.wikimedia.org/wiki/File:MIT_logo.svg">Massachusetts Institute of Technology</a> (vectorized by <a target="_blank" href="https://en.wikipedia.org/wiki/User:Mysid">Mysid</a>, modified by [whinee](https://github.com/whinee)), Public domain, via Wikimedia Commons

<h2 id="attribution-icons"><b><i><a href="#attribution-icons">Icons</a></i></b></h2>

<a target="_blank" href="https://icons8.com/icon/102502/exclamation-mark">Exclamation Mark</a>, <a target="_blank" href="https://icons8.com/icon/33294/code-fork">Code Fork</a>, <a target="_blank" href="https://icons8.com/icon/85185/star">Star</a>, <a target="_blank" href="https://icons8.com/icon/34095/group">Group</a>, <a target="_blank" href="https://icons8.com/icon/87276/code">Code</a>, and <a href="https://icons8.com/icon/30888/discord">Discord</a> icons by <a target="_blank" href="https://icons8.com">Icons8</a>

<sub>
    <i>
        <b>NOTE:</b> If a reference or source material is not attributed properly or not at all, please kindly message me at Discord: <a target="_blank" href="https://discord.com/users/848092597822160907">whi_ne#4783</a> or create a pull request so I can properly give credit to their respective authors.
    </i>
</sub>

<h2 id="further-reading"><b><a href="#further-reading">Further Reading</a></b></h2>

- [Frequently Asked Questions](faq.md)
- [License Agreement](license.md)
- [Latest Documentation (0.0.x.x)](docs/0/0/index.md)
- [All Documentation](docs/index.md)
- [Changelog](changelog.md)
- [Latest Bump](latest-bump.md)
- [Latest Commit](latest-commit.md)
- [Notes for whi~nyaan!](notes-to-self.md)
- [whi~nyaan!'s diary](diary.md)
