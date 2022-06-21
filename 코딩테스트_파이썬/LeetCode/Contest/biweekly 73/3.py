import copy
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        rets =[]

        for i in range(n):
            rets.append([])

        for edge in edges:
            rets[edge[1]].append(edge[0])

        for i in range(len(rets)):
            q = copy.deepcopy(rets[i])

            while q:
                now = q.pop()
                for j in rets[now]:
                    if j not in rets[i]:
                        q.append(j)
                        rets[i].append(j)

        for ret in rets:
            ret.sort()
        return rets


a = Solution()
a.getAncestors(1000,
[[504,505],[179,180],[735,736],[824,825],[188,189],[163,164],[476,477],[956,957],[733,734],[917,918],[936,937],[959,960],[669,670],[211,212],[140,141],[450,451],[160,161],[864,865],[652,653],[694,695],[925,926],[579,580],[927,928],[148,149],[876,877],[328,329],[552,553],[785,786],[227,228],[510,511],[752,753],[599,600],[886,887],[659,660],[274,275],[871,872],[797,798],[667,668],[6,7],[77,78],[753,754],[539,540],[151,152],[272,273],[813,814],[954,955],[61,62],[310,311],[175,176],[214,215],[157,158],[614,615],[641,642],[921,922],[513,514],[118,119],[266,267],[719,720],[182,183],[769,770],[770,771],[540,541],[390,391],[15,16],[543,544],[518,519],[644,645],[939,940],[575,576],[996,997],[897,898],[380,381],[472,473],[817,818],[975,976],[972,973],[646,647],[35,36],[416,417],[242,243],[250,251],[347,348],[961,962],[392,393],[682,683],[894,895],[489,490],[940,941],[574,575],[216,217],[711,712],[997,998],[417,418],[922,923],[689,690],[63,64],[685,686],[75,76],[459,460],[451,452],[177,178],[889,890],[700,701],[603,604],[780,781],[460,461],[768,769],[888,889],[577,578],[645,646],[434,435],[308,309],[224,225],[631,632],[945,946],[582,583],[617,618],[444,445],[324,325],[383,384],[887,888],[911,912],[923,924],[254,255],[783,784],[722,723],[742,743],[294,295],[965,966],[344,345],[903,904],[681,682],[349,350],[757,758],[205,206],[545,546],[601,602],[811,812],[0,1],[481,482],[688,689],[537,538],[710,711],[295,296],[173,174],[340,341],[66,67],[746,747],[589,590],[974,975],[859,860],[915,916],[814,815],[835,836],[848,849],[208,209],[81,82],[810,811],[20,21],[815,816],[359,360],[496,497],[237,238],[508,509],[48,49],[716,717],[661,662],[968,969],[428,429],[514,515],[291,292],[233,234],[111,112],[393,394],[110,111],[162,163],[980,981],[832,833],[299,300],[355,356],[623,624],[947,948],[739,740],[896,897],[604,605],[180,181],[717,718],[176,177],[402,403],[713,714],[125,126],[962,963],[105,106],[440,441],[863,864],[130,131],[979,980],[388,389],[26,27],[108,109],[781,782],[360,361],[731,732],[281,282],[891,892],[309,310],[240,241],[92,93],[506,507],[846,847],[709,710],[734,735],[967,968],[844,845],[671,672],[767,768],[362,363],[725,726],[827,828],[463,464],[638,639],[839,840],[58,59],[269,270],[475,476],[592,593],[45,46],[33,34],[181,182],[113,114],[34,35],[693,694],[314,315],[264,265],[456,457],[892,893],[464,465],[73,74],[933,934],[377,378],[172,173],[80,81],[255,256],[738,739],[495,496],[796,797],[572,573],[882,883],[372,373],[826,827],[538,539],[116,117],[126,127],[350,351],[469,470],[955,956],[441,442],[932,933],[803,804],[983,984],[257,258],[642,643],[516,517],[901,902],[432,433],[548,549],[718,719],[168,169],[881,882],[278,279],[244,245],[333,334],[515,516],[581,582],[910,911],[312,313],[238,239],[193,194],[129,130],[437,438],[263,264],[750,751],[904,905],[435,436],[122,123],[289,290],[666,667],[500,501],[677,678],[564,565],[673,674],[413,414],[966,967],[919,920],[119,120],[2,3],[942,943],[724,725],[493,494],[329,330],[470,471],[404,405],[356,357],[204,205],[479,480],[3,4],[893,894],[969,970],[156,157],[351,352],[656,657],[895,896],[123,124],[941,942],[466,467],[651,652],[446,447],[633,634],[747,748],[531,532],[926,927],[703,704],[593,594],[981,982],[471,472],[239,240],[403,404],[866,867],[946,947],[809,810],[586,587],[86,87],[376,377],[128,129],[964,965],[924,925],[878,879],[562,563],[296,297],[247,248],[10,11],[249,250],[19,20],[378,379],[831,832],[721,722],[306,307],[279,280],[794,795],[916,917],[419,420],[400,401],[503,504],[439,440],[262,263],[720,721],[840,841],[870,871],[62,63],[465,466],[517,518],[54,55],[290,291],[453,454],[668,669],[414,415],[367,368],[14,15],[755,756],[944,945],[184,185],[411,412],[194,195],[366,367],[342,343],[96,97],[462,463],[106,107],[79,80],[330,331],[477,478],[138,139],[161,162],[331,332],[563,564],[977,978],[649,650],[847,848],[449,450],[87,88],[547,548],[191,192],[445,446],[883,884],[512,513],[155,156],[736,737],[542,543],[691,692],[970,971],[976,977],[374,375],[998,999],[490,491],[401,402],[530,531],[71,72],[134,135],[112,113],[38,39],[664,665],[99,100],[898,899],[431,432],[358,359],[298,299],[729,730],[554,555],[93,94],[12,13],[379,380],[234,235],[375,376],[687,688],[988,989],[935,936],[83,84],[186,187],[958,959],[578,579],[74,75],[387,388],[984,985],[828,829],[320,321],[84,85],[994,995],[627,628],[91,92],[692,693],[790,791],[143,144],[585,586],[985,986],[137,138],[253,254],[458,459],[98,99],[154,155],[207,208],[202,203],[784,785],[293,294],[385,386],[834,835],[11,12],[384,385],[805,806],[322,323],[313,314],[949,950],[198,199],[556,557],[280,281],[307,308],[775,776],[252,253],[72,73],[536,537],[370,371],[816,817],[478,479],[485,486],[804,805],[885,886],[285,286],[732,733],[4,5],[346,347],[647,648],[391,392],[812,813],[436,437],[220,221],[363,364],[345,346],[765,766],[918,919],[497,498],[971,972],[943,944],[744,745],[541,542],[868,869],[908,909],[348,349],[798,799],[751,752],[335,336],[505,506],[634,635],[782,783],[145,146],[565,566],[862,863],[605,606],[95,96],[268,269],[748,749],[737,738],[273,274],[336,337],[788,789],[30,31],[861,862],[626,627],[535,536],[995,996],[712,713],[608,609],[267,268],[304,305],[139,140],[569,570],[758,759],[773,774],[164,165],[315,316],[190,191],[707,708],[854,855],[929,930],[43,44],[259,260],[640,641],[934,935],[484,485],[94,95],[850,851],[282,283],[199,200],[705,706],[629,630],[89,90],[880,881],[884,885],[704,705],[931,932],[650,651],[607,608],[600,601],[553,554],[286,287],[905,906],[327,328],[319,320],[874,875],[621,622],[494,495],[588,589],[558,559],[743,744],[590,591],[594,595],[461,462],[271,272],[165,166],[606,607],[25,26],[584,585],[683,684],[597,598],[771,772],[648,649],[339,340],[408,409],[657,658],[662,663],[243,244],[31,32],[265,266],[655,656],[338,339],[818,819],[571,572],[960,961],[483,484],[394,395],[37,38],[900,901],[424,425],[879,880],[628,629],[992,993],[284,285],[121,122],[613,614],[454,455],[405,406],[786,787],[109,110],[636,637],[622,623],[573,574],[760,761],[457,458],[241,242],[57,58],[248,249],[131,132],[24,25],[321,322],[334,335],[341,342],[368,369],[802,803],[171,172],[522,523],[226,227],[741,742],[185,186],[492,493],[52,53],[561,562],[422,423],[332,333],[69,70],[665,666],[64,65],[774,775],[928,929],[772,773],[529,530],[544,545],[78,79],[219,220],[653,654],[146,147],[792,793],[763,764],[60,61],[399,400],[141,142],[583,584],[50,51],[438,439],[409,410],[59,60],[337,338],[229,230],[702,703],[183,184],[596,597],[192,193],[521,522],[261,262],[167,168],[953,954],[102,103],[822,823],[357,358],[82,83],[276,277],[373,374],[906,907],[218,219],[680,681],[658,659],[706,707],[425,426],[789,790],[452,453],[591,592],[948,949],[468,469],[364,365],[860,861],[178,179],[56,57],[875,876],[215,216],[115,116],[217,218],[498,499],[174,175],[149,150],[611,612],[70,71],[447,448],[41,42],[507,508],[127,128],[343,344],[532,533],[325,326],[825,826],[519,520],[53,54],[144,145],[22,23],[29,30],[756,757],[806,807],[398,399],[723,724],[527,528],[830,831],[288,289],[877,878],[395,396],[65,66],[382,383],[618,619],[567,568],[845,846],[730,731],[632,633],[195,196],[67,68],[275,276],[200,201],[615,616],[799,800],[708,709],[222,223],[228,229],[899,900],[938,939],[235,236],[777,778],[8,9],[546,547],[670,671],[609,610],[990,991],[920,921],[311,312],[684,685],[630,631],[427,428],[433,434],[189,190],[147,148],[187,188],[913,914],[851,852],[576,577],[153,154],[616,617],[245,246],[455,456],[46,47],[365,366],[852,853],[21,22],[793,794],[97,98],[418,419],[858,859],[701,702],[675,676],[778,779],[209,210],[595,596],[855,856],[524,525],[989,990],[232,233],[421,422],[480,481],[533,534],[754,755],[930,931],[624,625],[865,866],[297,298],[225,226],[231,232],[442,443],[690,691],[619,620],[740,741],[907,908],[499,500],[557,558],[23,24],[857,858],[610,611],[317,318],[686,687],[676,677],[166,167],[117,118],[745,746],[486,487],[473,474],[420,421],[76,77],[872,873],[206,207],[549,550],[902,903],[28,29],[236,237],[443,444],[491,492],[487,488],[369,370],[801,802],[714,715],[695,696],[197,198],[103,104],[957,958],[914,915],[287,288],[993,994],[679,680],[762,763],[779,780],[551,552],[761,762],[474,475],[678,679],[142,143],[566,567],[726,727],[114,115],[305,306],[397,398],[663,664],[256,257],[550,551],[833,834],[302,303],[787,788],[986,987],[203,204],[42,43],[635,636],[361,362],[978,979],[39,40],[90,91],[100,101],[598,599],[150,151],[201,202],[158,159],[842,843],[841,842],[620,621],[823,824],[488,489],[323,324],[212,213],[795,796],[660,661],[159,160],[303,304],[169,170],[223,224],[353,354],[856,857],[40,41],[371,372],[728,729],[423,424],[819,820],[107,108],[283,284],[570,571],[251,252],[396,397],[526,527],[9,10],[808,809],[124,125],[120,121],[672,673],[836,837],[135,136],[963,964],[867,868],[869,870],[136,137],[973,974],[17,18],[699,700],[568,569],[937,938],[502,503],[386,387],[277,278],[88,89],[407,408],[580,581],[7,8],[509,510],[18,19],[260,261],[987,988],[534,535],[221,222],[849,850],[501,502],[838,839],[625,626],[101,102],[587,588],[697,698],[381,382],[301,302],[430,431],[448,449],[843,844],[85,86],[412,413],[612,613],[821,822],[829,830],[170,171],[696,697],[16,17],[820,821],[316,317],[426,427],[560,561],[982,983],[602,603],[210,211],[715,716],[352,353],[213,214],[511,512],[523,524],[951,952],[13,14],[467,468],[44,45],[318,319],[104,105],[791,792],[49,50],[800,801],[354,355],[853,854],[36,37],[246,247],[776,777],[406,407],[292,293],[950,951],[51,52],[415,416],[27,28],[991,992],[525,526],[807,808],[230,231],[912,913],[389,390],[410,411],[890,891],[47,48],[5,6],[326,327],[1,2],[133,134],[55,56],[639,640],[520,521],[952,953],[654,655],[482,483],[258,259],[196,197],[152,153],[873,874],[643,644],[674,675],[68,69],[727,728],[698,699],[759,760],[749,750],[637,638],[32,33],[837,838],[270,271],[559,560],[132,133],[429,430],[300,301],[909,910],[528,529],[764,765],[766,767],[555,556]])