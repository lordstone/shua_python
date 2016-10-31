class Solution(object):
    def dfs(self, cur, pDict):
        if tuple(cur) in self.dp:
            return []
        res = []

        if len(cur) == self.n:
            return [cur]
        elif len(cur) == 0:  # begin phase
            for w in self.words:
                nextPDict = []
                for c in w:
                    if c not in pDict:
                        break
                    nextPDict.append(pDict[c])
                if len(nextPDict) == self.n:
                    res += self.dfs([w], nextPDict)
        else:  # continue
            for w in self.words:
                nextPDict = []
                idx = len(cur)
                signal = False
                # see if the selected word qualifies
                # check first half
                for j in range(idx):
                    if w[j] != cur[j][idx]:
                        signal = True
                        break

                if signal is True:
                    continue

                for i, c in enumerate(w):  # w[i] is the char
                    if c not in pDict[i]:
                        break
                    nextPDict.append(pDict[i][c])
                if len(nextPDict) == self.n:
                    nextCur = cur[:]
                    nextCur.append(w)
                    res += self.dfs(nextCur, nextPDict)
        self.dp[tuple(cur)] = res
        return res

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if len(words) == 0:
            return []
        self.n = len(words[0])
        self.words = words
        self.dp = dict()

        # creating trie
        self.trie = dict()
        for w in words:
            cur = self.trie
            for i in range(len(w) - 1):
                if w[i] not in cur:
                    cur[w[i]] = dict()
                cur = cur[w[i]]
            if w[-1] not in cur:
                cur[w[-1]] = 0
            cur[w[-1]] += 1

        res = self.dfs([], self.trie)
        # res.sort()
        return res

class SolutionBest(object):

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        m = len(words)
        n = len(words[0]) if m else 0
        import collections
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)
        matrix = []
        ans = []
        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in mdict[prefix]:
                    search(word, line + 1)
            matrix.pop()
        for word in words:
            search(word, 1)
        return ans

sol = SolutionBest()

# words = ['abaa', 'babb']
words = ["ldqv","tibp","koey","dsdh","wxjz","glam","eyyy","ymeo","yjjp","qqjq","qsra","eldf","fcgc","fuqs","awgs","wcjp","pafp","amlz","uzql","rtre","sxur","frvx","lvwn","zbfv","ekfe","ugac","mqel","ryzg","uxfb","urea","vdir","xxeg","ipuq","vuxx","nzou","bsid","aows","schd","bkto","jrpm","cctl","koiu","vzaf","viuc","gnwm","sdvg","gvyu","bqkl","mtvj","wwpp","cyhe","hqpi","enoq","puhc","aknu","vwbg","bafk","bnhg","gcny","xdap","zmgr","pdpj","kpef","trms","miwe","bakx","vpbr","naiw","xlzj","bocb","tyyk","osqw","hhia","scer","igjz","tvsy","oron","tlqz","leyz","mgwb","ebbo","vmwm","nuxb","gunb","tjuj","oezm","spro","bjzo","jnjx","ucbu","yfpw","fmhl","xkfp","bnij","ihwn","fvci","isxg","svim","msyg","sjfs","rczg","vioc","ywrg","ebkr","noiu","hkhc","udtr","kxdf","qxgk","jziu","hjwb","oulh","kidq","mzks","rekt","pnye","bhup","vwwv","bxop","hyvv","aoae","ephf","fixl","jpjq","wzmb","ygzw","hyva","cjgu","ojxa","ovaw","jznc","duct","aotz","ryor","rchy","wktq","mwtt","ougt","lkks","zraz","jghv","oecr","icej","szfa","cilr","rhej","rgwm","mzws","lymr","htch","abva","vfhw","lgbz","igud","warz","grti","xycf","ffel","kqqs","pmyx","hxub","vdma","tdph","fxfw","drpf","yial","vgwr","uary","rdgu","kyoj","ygfg","yvet","muzi","vydu","sabk","cylc","eiys","ozfz","sdrq","xwnf","laqb","apfd","tqci","gpvm","qxbn","ednm","qara","iawb","lzvs","spvv","hdbq","mrgu","mkfy","hxdt","qczg","nxwy","uzlm","jfde","nwao","satz","ruoz","sruw","iwnk","dclt","smss","lhto","hihh","zrsq","xjfe","jxkf","wgpb","ptfl","hnjz","yxjq","yqyk","xeib","mjpo","blhi","xksx","smju","xazs","zujb","xrmt","nrgs","zimw","dove","rzjk","rhbl","doaz","pdnx","tktr","fgzd","jdcs","yuqv","tlch","mdak","fybt","ewzh","inza","qakq","zkma","rrga","falm","ngxs","xbda","xbdg","nsfm","uqvi","exft","eozp","fabz","azbc","wmpb","ctpn","udhn","yvxk","pqxr","zcde","zbsh","vgzv","qdot","ozeu","jcdn","uvri","maib","kxml","nytx","vwac","pzhx","poqa","vjeq","grph","skqt","eyak","yqle","yhpe","urmq","wmnj","eupp","juav","lzab","vpga","jmho","icpv","hgak","oqzp","jhce","trkw","foog","bnvj","teri","sevi","pgaf","hugy","llpn","xrcz","fjya","ydjh","ckzr","xhcn","eeyw","ckzx","ietb","gtah","wnut","knzc","ahvp","aqbh","dxmf","eeyc","wzwi","uakc","yeap","exyh","kanw","ygum","ytfn","hhak","wbrl","bvcb","ogzh","ufax","cvxp","jpkc","bhff","mgws","ybiz","daph","abhn","bvjf","xtma","ukuw","dapu","qigj","blmj","loic","mnaw","qlyv","ycsz","fkua","dhzg","ctwf","ejui","ayrt","wxiy","zsng","vjpq","gvjc","epyg","xnmk","rwaa","gjzb","jhqd","yurf","lwek","xnme","xyur","ufsd","bmhc","wwwc","atjg","voos","ofjq","owhc","oklh","dejn","lzdb","szla","mrxq","hssr","oicv","cads","oafg","uvvk","yonk","xohx","voic","wekh","yygg","odtz","criz","qcps","vxfg","thjz","gbgx","gkcq","bgjz","yxfy","yggl","lclm","rqbb","kftb","wekb","xzir","kmqv","fpwy","kipl","fvgt","kmqh","ovnm","rfiq","vhjo","hvcg","wpwf","rgvt","tkyl","zyyz","exkq","dynw","uvug","unqa","rjqm","nfsi","rogj","fqvr","zxtj","eamr","oxap","tmoh","qels","ntic","zmsu","htzi","lxbe","cemy","sxae","qppg","vndx","tbbc","jtjn","zezb","fctj","irud","vgkh","zsad","aeqn","pxsa","mywd","lktx","lyzn","uhqh","qheo","qylj","twxv","kffg","wrio","nebh","tsga","omfr","kkep","qgqe","bppz","ojrx","ilqs","fgcb","sayj","spga","qbtt","jnzf","uuxa","bsfw","djwd","jygn","tzwv","dmco","hofl","lrqy","thty","xibo","mgek","aexq","wgxs","eega","swcp","rvxo","essd","opxr","foph","yqqb","uqxh","tmtn","syac","rvxj","ycex","xwpi","lbih","jqwg","cfmy","erbk","ycku","fiej","oghu","erbo","uyug","nmif","denc","toik","owdd","hbxf","fhkh","jksd","dnbn","ujem","rlwc","oojq","vzqc","vsxh","wrzv","xmlu","qeiw","vebr","jgrz","bgdg","bjqc","xnuk","kwti","aiwc","evnv","gttd","ntma","ffdo","ublq","fjzw","cgya","jukv","hwvx","rblz","uyvg","gkil","ukoe","ainn","lekg","jwcc","xndl","tnvd","sskz","ibka","hkvn","jdno","yvir","kwvu","npzu","zwpe","mguj","gxsl","awfx","rlbe","dlxw","ehvp","gpuu","leud","dqet","tqkg","pwwe","lyqz","hcay","graj","jaqb","raxj","snfq","rpij","vffm","fnlo","ymki","etik","sipm","lkoi","tcnq","oxpd","kvac","yaxe","xmvv","izxo","foss","yzgd","dgub","gnhj","nqpg","htai","zbny","rlld","kmom","uyoy","joyw","mvcd","fcmm","gagc","qrdf","vprp","gkur","joyd","rvyz","ywip","tihz","udbx","hfhs","jxdo","vhtq","jmri","snpv","fvmi","yumq","mqhb","rccb","ixud","zhxb","bzoz","pkpb","opag","axzf","nlkk","ilmm","xqyu","xgvz","zxim","sjvz","wjsj","khew","oxjb","giri","tavh","xffa","aasl","zngx","ygoi","mvor","zdwq","yhwn","vxys","jbud","jxgu","kpkz","tmnk","xjxg","nqbg","zfwt","zpee","coqp","iyrz","zklv","dgvg","fbqo","vpkz","aijr","yeog","iyru","xemr","qqft","jtkj","omwr","vfbz","yizn","qqfs","dcip","whog","noeg","gwii","wkje","hhbz","exrl","cmyx","bulm","gjqy","uahk","davi","okjn","jhvc","gwwp","rvdu","eeqd","rsje","vlco","lhqj","bjdq","hnou","pqdf","jzbv","iobg","eyqb","hoam","rzzy","ctrc","hoab","yidi","ypup","mpqj","cjrf","kzib","xhvp","gimw","zsig","nlpm","mdxk","jftn","fkpj","eajd","pxbh","lyks","zopy","apcl","kxoo","ecpu","uzuc","jouj","kxog","cfdn","aktr","udfu","lgvc","oiny","uwci","fefg","oago","btdy","ofvg","vzla","fedn","cpts","ewfy","thkl","dfwm","xxgb","zqle","ungi","ngmr","ooip","fxdp","eviy","shjs","cuqu","ygan","qwvi","pwru","xnyc","wpvw","ojhz","okqg","nolf","kwht","osdv","kfwp","mmvr","skzx","mwda","dghb","bvvh","qlcu","adbc","hesk","rypw","dezb","jjqd","irbf","wqqi","tlwz","nwfx","ntuq","wqqu","zkvu","hdlw","hzfx","czvw","uqli","alum","zqgp","cbbk","lfeh","wagb","vrpl","snny","gfzg","chps","edyc","mzle","mpcg","qous","upyn","natl","ftco","ukmc","kbtf","upye","fgbf","frcm","ytdu","srlb","ycqu","pfbs","gamy","ditz","bceh","nedl","bmpc","xxab","uquk","gmvi","gamn","qtgn","imln","bvox","uela","xzza","ydsw","fqbu","zgoi","pfcu","pdil","kuln","aeyy","oade","wlco","euwh","dhsq","htii","blys","jtzg","yrvb","lcef","qrlq","dzcz","kbxs","urbt","xgqq","xasg","ucsu","hhqa","txzd","ozgk","mook","rohf","hojd","fema","gsfj","edby","lvdg","czxq","bbyl","yiwb","rkie","vedk","pueg","yksc","lvdm","ghsi","lswv","ttjt","rdaf","uezp","ndbp","lsbr","phel","anwe","mjcz","ngfs","mkei","tixh","oyvx","lxyx","xftd","aeol","iwaj","nnlg","trgg","gefc","bgln","nmnr","cmal","rqic","nnlp","rqif","slkq","ylzq","mazo","wepn","hqnd","hkmx","onxu","zukm","yrcp","qerl","dowl","ehsu","efyv","fzpi","mfny","vtfv","hzbw","zlvt","gjmv","smbe","wwhz","qzrz","ugml","rowz","pylj","nsji","imij","cjat","sojk","lzcy","jzcq","rowk","bcsz","ecqy","witq","kjxi","eeih","ymha","mzon","yjtl","vwws","kcwe","rvrf","pmph","uzvk","pxho","uszb","csox","byor","ovge","zotp","mebc","iisf","xjkm","zarv","nkfx","flih","jxbc","wisy","zptw","gtqn","orxa","wnum","ttlg","qsgz","cafz","eusu","cqqh","dmun","tnhw","royc","tftk","yagc","sftr","usfr","wcid","teza","isdg","ckog","dysy","rjbi","ltlm","mlol","yzsg","ptkt","doyr","rbri","okva","skiu","iwfr","ebfv","tojg","uvmr","pzbe","wnij","iezr","sdcg","kpan","mfec","cmfx","bfen","ulai","exrm","jaxf","vfdr","nxvk","iodt","vcdd","epbo","tbie","mnuw","qjay","edop","ioav","ohkj","ucmh","vqss","oavy","eeak","egwg","sljt","xnam","ffab","puse","znoq","pmhf","bjrl","syxs"]
print(sol.wordSquares(words))
