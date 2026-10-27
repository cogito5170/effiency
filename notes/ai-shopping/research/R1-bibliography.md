# R1 서지 검증

검증일 2026-10-27 · 대상: [이론 기반 검토 문서](https://claude.ai/artifact/VwqhX7QXNhYj5Z1pMGdUMo)의 학술 문헌 26편

## 방법과 한계

각 문헌을 웹 검색으로 찾아 RePEc(IDEAS), 출판사(INFORMS·CVF·PMLR·NeurIPS), 저자 소속 기관 저장소의 서지 레코드와 대조했다.
Crossref API는 이 환경의 네트워크 정책에서 막혀 있어 DOI 레졸버로 직접 확인하지는 못했다.
판정은 세 단계로 나눴다.

- **A** 제목·연도·권·호(또는 학회)·쪽을 색인 레코드에서 확인
- **B** 제목·연도·학술지를 확인했고 권·호·쪽은 색인 화면에서 직접 보지 못함
- **수정** 검토 문서의 표기를 고쳐야 함

## 결과 요약

26편 모두 실재하며, 저자·연도·학술지가 틀린 문헌은 없다. 부제가 빠진 6편은 정식 제목으로 고친다.
권·호·쪽까지 색인에서 직접 확인한 것은 18편이고, 8편은 B 등급이다.

## 판정표

| # | 문헌 | 판정 | 확인 근거 | 비고 |
|---|---|---|---|---|
| 1 | Stigler (1961) *JPE* 69(3) | B | 검색 결과에 서지 레코드 미노출 | 쪽 213–225로 알려져 있으나 이번에 직접 보지 못함 |
| 2 | Weitzman (1979) *Econometrica* 47(3) | A | [Econometric Society](https://econometricsociety.org/publications/econometrica/1979/05/01/optimal-search-best-alternative) (1979년 5월호) | |
| 3 | Bakos (1997) *Management Science* 43(12) | A | [RePEc](https://ideas.repec.org/a/inm/ormnsc/v43y1997i12p1676-1692.html), pp. 1676–1692 | |
| 4 | Brynjolfsson, Hu & Simester (2011) *Management Science* 57(8) | A | [INFORMS](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.1110.1371), DOI 10.1287/mnsc.1110.1371 | **수정** 부제 추가: "…: The Effect of Search Costs on the Concentration of Product Sales" |
| 5 | Caillaud & Jullien (2003) *RAND JE* 34(2) | A | [RePEc](https://ideas.repec.org/a/rje/randje/v34y2003i2p309-28.html), pp. 309–328 | |
| 6 | Rochet & Tirole (2003) *JEEA* 1(4) | A | [RePEc](https://ideas.repec.org/a/tpr/jeurec/v1y2003i4p990-1029.html), pp. 990–1029 | |
| 7 | Armstrong (2006) *RAND JE* 37(3) | A | [RePEc](https://ideas.repec.org/a/rje/randje/v37y20063p668-691.html), pp. 668–691 | |
| 8 | Eisenmann, Parker & Van Alstyne (2011) *SMJ* 32(12) | B | [HBS Working Knowledge](https://hbswk.hbs.edu/item/platform-envelopment), [EconBiz](https://econbiz.de/Record/platform-envelopment-eisenmann-thomas/10009376673) | |
| 9 | Farrell & Klemperer (2007) *Handbook of IO* Vol. 3 | A | [RePEc](https://ideas.repec.org/r/eee/indchp/3-31.html), 3권 31장 | |
| 10 | Iyengar & Lepper (2000) *JPSP* 79(6) | B | [PubPeer](https://pubpeer.com/publications/8D13EB09E616D324577F77D68645F2), [AcaWiki](https://acawiki.org/When_Choice_is_Demotivating:_Can_One_Desire_Too_Much_of_a_Good_Thing%3F) | **수정** 부제 추가: "…: Can One Desire Too Much of a Good Thing?" |
| 11 | Scheibehenne, Greifeneder & Todd (2010) *JCR* 37(3) | A | [RePEc](https://ideas.repec.org/a/oup/jconrs/v37y2010i3p409-425.html), pp. 409–425 | |
| 12 | Chernev, Böckenholt & Goodman (2015) *JCP* 25(2) | B | [Kellogg](https://www.kellogg.northwestern.edu/faculty/research/detail/2015/when-product-assortment-leads-to-choice-overload-a-conceptual), [Scinapse](https://www.scinapse.io/papers/2087356051) | Kellogg 페이지 주소에는 다른 제목(작업 제목으로 추정, `[판단]`)이 보임. 출판 제목은 문서 표기와 같음 |
| 13 | Bettman, Luce & Payne (1998) *JCR* 25(3) | A | [RePEc](https://ideas.repec.org/a/oup/jconrs/v25y1998i3p187-217.html), pp. 187–217 | |
| 14 | Shampanier, Mazar & Ariely (2007) *Marketing Science* 26(6) | A | [RePEc](https://ideas.repec.org/a/inm/ormksc/v26y2007i6p742-757.html), pp. 742–757, DOI 10.1287/mksc.1060.0254 | **수정** 부제 추가: "…: The True Value of Free Products" |
| 15 | Lambrecht & Skiera (2006) *JMR* 43(2) | B | [London Business School](https://www.london.edu/faculty-and-research/academic-research/p/paying-too-much-and-being-happy-about-it-existence-causes-and-con) | |
| 16 | Ursu (2018) *Marketing Science* 37(4) | A | [RePEc](https://ideas.repec.org/a/inm/ormksc/v37y2018i4p530-552.html), pp. 530–552, DOI 10.1287/mksc.2017.1072 | |
| 17 | Ahlberg, Williamson & Shneiderman (1992) *CHI '92* | A | [UMD HCIL](https://lccd.umiacs.umd.edu/node/17103), DOI 10.1145/133160.133216 | **수정** 부제 추가: "…: An Implementation and Evaluation" |
| 18 | Shneiderman (1996) *IEEE Symp. Visual Languages* | A | [UMD DRUM](https://drum.lib.umd.edu/handle/1903/5784) | |
| 19 | Marchionini (2006) *CACM* 49(4) | A | [CACM 2006년 4월호](https://cacm.acm.org/issue/april-2006) | |
| 20 | Chen & Pu (2012) *UMUAI* 22 | B | [EPFL Infoscience](https://infoscience.epfl.ch/record/176775), [HKBU](https://scholars.hkbu.edu.hk/en/publications/critiquing-based-recommenders-survey-and-emerging-trends-2/) | |
| 21 | Jannach, Manzoor, Cai & Chen (2021) *ACM CSUR* 54(5) | B | [arXiv 2004.00646](https://arxiv.org/pdf/2004.00646), [HKBU](https://scholars.hkbu.edu.hk/en/publications/a-survey-on-conversational-recommender-systems/) | 권·호는 이번에 직접 보지 못함 |
| 22 | Fleder & Hosanagar (2009) *Management Science* 55(5) | B | [INFORMS](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.1080.0974), [Penn](https://repository.upenn.edu/oid_papers/152) | **수정** 부제 추가: "…: The Impact of Recommender Systems on Sales Diversity" |
| 23 | Liu 외 (2016) *CVPR* | A | [CVF Open Access](https://openaccess.thecvf.com/content_cvpr_2016/html/Liu_DeepFashion_Powering_Robust_CVPR_2016_paper.html) | **수정** 정식 제목 "…Retrieval with Rich Annotations" |
| 24 | Guo 외 (2018) *NeurIPS* | A | [NeurIPS Proceedings](https://papers.nips.cc/paper/7348-dialog-based-interactive-image-retrieval) | |
| 25 | Radford 외 (2021) *ICML* | A | [PMLR 139](https://proceedings.mlr.press/v139/radford21a.html) | |
| 26 | Wu 외 (2021) *CVPR* | A | [CVF Open Access](https://openaccess.thecvf.com/content/CVPR2021/html/Wu_Fashion_IQ_A_New_Dataset_Towards_Retrieving_Images_by_Natural_CVPR_2021_paper.html) | |

부제 누락은 인용의 진위에는 영향이 없지만, 정식 참고문헌에는 전체 제목을 쓴다. 4·10·14·17·22·23번 6편이 해당한다.

## 남은 일

- B 등급 8편은 DOI 레졸버나 출판사 페이지에서 권·호·쪽을 한 번 더 확인한다. Crossref를 열 수 있는 환경(Mac)에서 하면 빠르다.
- 본문 주장이 원문 결론과 맞는지(예: Chernev 외 2015의 조절변수 네 가지)는 R2~R4를 진행하면서 해당 논문 초록과 대조한다.
