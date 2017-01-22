

from methods import rotate as rot



def test_run():

    in_ = """abc
def
ghi"""
    expected = """gda
heb
ifc
"""

    print(rot.run(in_))
    assert rot.run(in_) == expected


def test_basics():

    in_ = """12
34
56"""
    expected = """531
642
"""

    print(rot.run(in_))
    assert rot.run(in_) == expected


def test_real():

    in_ = """
OsoxNIRNLvlFLGoVHvBl
zssiLjmdDonUFNQAMclU
FaydhxfbrljCofabHHrz
roGAIhwUinNEJrLMgvgM
lCjWcHHwfxihsCEqdMUy
TBHiqLaHYAUxlVSqWbTJ
YkujORBAETrvlCAoXFix
QTgSoXdKEMwNijEtXrrK
lCyIHuGwROohRKygebJs
HiVpxkkJWEhHAyDqscVZ
HxNhFxKTcKeiCQHKyVuS
DxCvYPYcMRyaQGJdNxht
GqKlOukLxFZjZQVFBPzR
idqMKGVLAeMIaWwVaDuw
nnjkJbnCHKYvOjufwtEo
TVeLilmAysgmrBnpRvUw
FAzQyspSCAMVFJeWJXzX
lkKvVCRHuCgCpxPLmoxW
bfYQzLKQqsIXsiHMEhDm
rZnAqCrduWcpigjTgFWQ
"""

    expected = """
rblFTniGDHHlQYTlrFzO
ZfkAVndqxxiCTkBCoass
nYKzejqKCNVyguHjGyso
AQvQLkMlvhpISjiWAdix
qzVyiJKOYFxHoOqcIhLN
CLCslbGuPxkuXRLHhxjI
rKRpmnVkYKkGdBaHwfmR
dQHSACLLcTJwKAHwUbdN
uquCyHAxMcWREEYfirDL
WsCAsKeFRKEOMTAxnlov
cIgMgYMZyehowrUiNjnl
pXCVmvIjaiHhNvxhECUF
ispFrOaZQCARillsJoFL
gixJBjWQGQyKjCVCrfNG
jHPenuwVJHDyEASELaQo
TMLWpfVFdKqgtoqqMbAV
gEmJRwaBNyseXXWdgHMH
FhoXvtDPxVcbrFbMvHcv
WDxzUEuzhuVJriTUgrlB
QmWXwowRtSZsKxJyMzUl
"""


    assert rot.run(in_).strip() == expected.strip()



def test_basics_2():
    in_ = """XrdaYlDYHJCOWrfIvfnz
yGEFrhirZqhESTrzeYQx
nTqxAvvYIQRivAtDMwmV
rVdLDlMNkAoMUsbLMYOv
mkYyclhPESHZDxSkLzUC
MFXuFoEcIAIXrZwfQgiD
MhvoeDytdldUVeAmWmeB
vrWJNosHCcUFBkkYfpwk
baFUYoTPFLmLNSBQgQcH
tDLDvRMcGVcxnhfKQkHo
tEfoykMcYwpKdDWQVffd
BmpSxGfuRfklPtBebnMt
OUqCBzHeZTSgoCdHQufX
mMcMGedVTjpeQwxJQWKn
iMSuoQPsuqjXtCiYoASK
lZHMLbZBaPZcvURgiOQm
qrcKnyDYSrXHzCQETnRp
BiUkXLPILdLVhdMwxkkO
xjYUutjkglJkCtaHGOfm
YqziGsJgYMjawNkuKVig"""
    expected = """YxBqlimOBttbvMMmrnyX
qjirZMMUmEDarhFkVTGr
zYUcHScqpfLFWvXYdqEd
iUkKMuMCSoDUJouyLxFa
GuXnLoGBxyvYNeFcDArY
stLybQezGkRooDollvhl
JjPDZPdHfMMTsyEhMviD
gkIYBsVeuccPHtcPNYrY
YgLSauTZRYGFCdIEkIZH
MldrPqjTfwVLclASAQqJ
jJLXZjpSkpcmUdIHoRhC
akVHcXeglKxLFUXZMiEO
wChzvtQoPdnNBVrDUvSW
NtdCUCwCtDhSkeZxsATr
kaMQRixdBWfBkAwSbtrf
uHwEgYJHeQKQYmfkLDzI
KGxTioQQbVQgfWQLMMev
VOknOAWunfkQpmgzYwYf
ifkRQSKfMfHcweiUOmQn
gmOpmKnXtdoHkBDCvVxz
"""
    assert rot.run(in_).strip() == expected.strip()
