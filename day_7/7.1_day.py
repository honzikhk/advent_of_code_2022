

only_sizes = {}

def read_data(input):
    with open(input, "r") as file:
        data = file.readlines()
        format_data = [line[0:len(line)-1] if line.endswith("\n") else line for line in data ]
        return format_data

data = read_data("day_7/7.1_day_input.txt")
# print(f"raw data: {data}")


def count_the_size_of_directories(formated_data):       # maybe delete this
    directories_size = {}
    only_names = []
    for command in formated_data:
        #name_of_directory = ""
        if command == "$ cd ..":
            continue
        elif command[0:4] == "$ cd":
            name_of_directory = command[5:]
            only_names.append(name_of_directory)
            directories_size[name_of_directory] = []
    return directories_size


directories_size = count_the_size_of_directories(data)
# print(f"dicts of sizes: {directories_size}")


def dummy_find_dirs(formated_data):
    all_dirrs = ["dir /"]
    for command in formated_data:
        if command[0:3] == "dir":
            all_dirrs.append(command)
    return all_dirrs

list_of_directories = dummy_find_dirs(data)
# print(f"all dirrs finded by dummy function: {list_of_directories}")


def make_system(formated_data):
    """ Create dictionary of name of dir as a key and list of content as value """
    fucking_dictionary = {}
    for command in range(0, len(formated_data)):
        _ = []
        expression = formated_data[command]
        if expression[2:4] == "ls":
            for command_2 in range(command + 1, len(formated_data)):
                if formated_data[command_2][0] == "$":
                    break
                else:
                    _.append(formated_data[command_2])

            fucking_dictionary[formated_data[command - 1][5:]] = _
    # fucking_dictionary[formated_data[command - 1][5:]] = _

    return fucking_dictionary


system_in_dict = {'/': ['dir dfmhjhd', '307728 ghpqs', 'dir hztjntff', 'dir rvstq', 'dir sjt', '120579 whhj.pqt', 'dir wrmm'], 'dfmhjhd':
['301486 ngtqtf', '13488 wfgqtw.sqr'], 'hztjntff': ['146900 ncgnjp.zqb', '123665 zjnll.zjl'], 'cwsf': ['18202 ngmsjfj.bvs', '124907 snhqbcqc', '149910 snj.ltq', '253218 vppzwd.ztb', 'dir wlpcb'], 'msr': ['272198 hwtj'], 'sthqhrc': ['45847 vzntwhzl.htf'], 'rvstq': ['9707 bqg', '296975 frcqrdm', '232225 hztjntff', '29794 ldmtcrq.dcs', 'dir nzdgz', 'dir vtlj', 'dir wmjbt', 'dir wrmm', '28366 wrmm.cjh', 'dir wrsmnpwf'], 'nzdgz': ['dir qscww', 'dir tdthnm'], 'fplqm': ['dir cwsf', 'dir cwzstq', '216299 mdcnwnng', '109253 nzdgz'], 'fld': ['dir jdpz', 'dir trjltfq'], 'jdpz': ['299969 fvgpbf.lps'], 'trjltfq': ['30081 tdzjl.jrw'], 'cwzstq': ['305925 gjfbqpr.jjv'], 'hzpqfj': ['119289 hwtj', '108285 lsb', '246049 svttl.bml', 'dir sztz', '75119 zjnll.zjl', '200316 zwj'], 'sztz': ['dir mjmbld', 'dir nzdgz', 'dir wrmm'], 'mjmbld': ['101870 hwtj'], 'wrmm': ['212937 frcqrdm', '153487 zjnll.zjl'], 'tfdnvnn': ['108268 vwtj'], 'jcszc': ['94496 frcqrdm', '247067 vmhfdm.lrc'], 'nzwzq': ['6875 dbqbstqp'], 'prbptvql': ['177069 zjnll.zjl'], 'tnpshhml': ['227272 jjdplm.wjb'], 'tsjsfg': ['dir fjhjl', '215211 hwtj', '4695 lsb', '250283 lvssbtc.fwq'], 'fjhjl': ['54983 swqt.jsm'], 'vtlj': ['103236 cmwpcdrj.zlc', '1640 fllj.vfg', '155765 frcqrdm', '250655 hwtj', 'dir hztjntff', '82919 hztjntff.gzd', 'dir tzwfnn', 'dir wrmm'], 'tzwfnn': ['dir grznq'], 'grznq': ['282278 pwmsds.vzr'], 'wmjbt': ['dir bpqjsnr', 'dir bqg', 'dir cwsf', '31392 ths.lpc', 'dir vlhr', 'dir wrmm', 'dir zgljrz', 'dir zgt'], 'bpqjsnr': ['dir bqg', '132830 fjp'], 'bqg': ['96072 zdh.gpp'], 'hljm': ['dir clblt'], 'clblt': ['dir qdjj', '47245 vzrpqlgs.zng', '181205 wpcp.rcw'], 'qdjj': ['152548 rcjzld.zfv'], 'jvzn': ['265757 clvj.bmr'], 'vlhr': ['156011 nzdgz.gct'], 'bstnjc': ['11588 lsb'], 'ljpn': ['dir cgghhhlf', '204262 gzh.gww', '171620 lqtbm.zbg', 'dir qfwrrp', 'dir smpltb'], 'cgghhhlf': ['14765 nvbvs.bnv'], 'qfwrrp': ['256670 hwtj'], 'smpltb': ['dir bgvfj'], 'bgvfj': ['65336 fprgmh.psg'], 'vzwtzl': ['53337 fggqjqvs'], 'wjsf': ['308476 nzsm.dfd', '99153 swhv.ghz', '241163 thpzp'], 'zgljrz': ['134867 fmndz.mhf'], 'zgt': ['132031 hwtj', '218404 zjnll.zjl'], 'clt': ['62449 jlwr.bds'], 'mjpw': ['147523 wrmm'], 'nlwpspl': ['dir bmmmhnbc', '244465 cqbq.qmw', '199707 hwtj', 'dir jjjdlj', '45952 lsb', '274021 mhprtvb.jnf', 'dir vctf'], 'bmmmhnbc': ['dir bldfbzr', 'dir cwsf', 'dir dmj', '202405 frcqrdm', '77128 hnrc.dqv', 'dir hztjntff', '242794 lqslmd', '198590 lsb', '87647 ngh.ljt', 'dir wmgwfvq'], 'bldfbzr': ['dir bqg', '224279 frcqrdm', '304382 hcfv.jpr', 'dir nzdgz', '24190 psvfl.hlg', 'dir qjzh', '95318 qpb.nzq'], 'nhmts': ['105545 cwhlrfv.rlz'], 'tqhthh': ['81739 sfmcss.rps', '14262 wmlmfzg.bqt'], 'qjzh': ['162159 cmn.rtc'], 'frc': ['dir wrmm'], 'ctrbwhpr': ['94535 wrmm.fjl'], 'shmjt': ['6523 svmsvg.vvc'], 'jbgrgz': ['152890 bnlprltj', '60156 dttwfgs', 'dir frvlnww', 'dir qszdtg'], 'frvlnww': ['297025 cjbnqm', '126118 mpnnb.wqb'], 'qszdtg': ['286900 fptpmp.fqb', '210489 qbpwdhqt.wtw'], 'dmj': ['dir bqg', '60042 gncqrjnr.nrp', 'dir rhd', '106478 smgjczbq.mbh'], 'rhd': ['104913 frcqrdm', '248815 lsb'], 'mczrpf': ['19896 frcqrdm', '273870 gvrb.lff', '281909 tht.bhc'], 'mzd': ['26174 sgbhjft'], 'wmgwfvq': ['130936 gzm.wzc', 'dir hztjntff', '61943 jdp', 'dir rvwhms'], 'vhdqhfqv': ['193016 qgr', '157253 vbrc'], 'grlgcgrl': ['164027 nzdgz.ptd'], 'nmm': ['101722 bqg'], 'tlrztbh': ['16955 cwsf', '196934 lvdsbss.lpr'], 'rvwhms': ['314729 bcgphtl.bsc'], 'jjjdlj': ['dir dnpf', 'dir mwlvndml'], 'dnpf': ['129865 pgczcz', '128274 zjtv.jml'], 'mwlvndml': ['dir nzdgz', '255297 vdsmgqdg.sbj'], 'vctf': ['dir bqg', '4316 cwsf.vnq', 'dir gcgqr', '139151 hztjntff', '270316 hztjntff.wng', '285602 mzzgnztv', '299195 nzdgz', 'dir vbqjbq'], 'gcgqr': ['71948 wbhbbr.rbg'], 'vbqjbq': ['dir sltqnp'], 'sltqnp': ['5768 nvdmjq', '20296 qtb.tcs', '303095 zndbj.pgm'], 'qwvjnwsf': ['118347 bqg.csn', 'dir hqlv', '107689 hwtj', '66314 nzdgz.dmw', '94334 sjc'], 'hqlv': ['250002 qcdpnc'], 'wrsmnpwf': ['205662 lsb'], 'sjt': ['dir cwsf', 'dir nzdgz', 'dir qsd',
'dir rdzsr', '66525 tqqvtzz.gzq', '260979 wnbvvz', 'dir zgrf', 'dir zmtmr'], 'dtpf': ['278443 frcqrdm', '138750 fslt.mmj'], 'fjtsb': ['142873 frcqrdm', '230248 lbhs', '116760 zjnll.zjl'], 'gdnnndj': ['dir sljmpls', 'dir zhn'], 'sljmpls': ['dir cnzhjqbm', 'dir cttgctwb', '307652 hwtj', 'dir rwwmcmt', '107266 zjnll.zjl'], 'cnzhjqbm': ['196818 frcqrdm'], 'cttgctwb': ['dir bqg'], 'rwwmcmt': ['77395 hcfv.jpr', '286056 nssl'],
'zhn': ['114122 dbcpsqn', 'dir mpfvnslm', 'dir zlqns'], 'mpfvnslm': ['dir qvtr'], 'qvtr': ['83650 bqg.qqh'], 'zlqns': ['36937 bgzjvvc.szm'], 'mfbp': ['199935 qwsb.vcd'], 'zclzqz': ['274497 zjnll.zjl'], 'qscww': ['224250 frcqrdm', '196936 hcfv.jpr'], 'tdthnm': ['dir hmq', 'dir tcdm'], 'hmq': ['172261 nhpfqc.tgj'], 'tcdm': ['188168 lsb'], 'qsd': ['dir bqg', 'dir pbfc'], 'mnrrmcc': ['33961 lsb'], 'pbfc': ['dir hwbdld'], 'hwbdld': ['178868 hztjntff.gql', '108145 stqzdh.zdn'], 'rdzsr': ['45590 zjnll.zjl'], 'zgrf': ['dir bqg', 'dir cbc', 'dir cclw', 'dir cwsf', 'dir fph', '258332 hcfv.jpr', 'dir hvvvv', 'dir hztjntff', '238272 nzwzmlqt.nvh', 'dir tqqqv'], 'cbc': ['119981 bznnrjtt', 'dir dsmmcjtg', '259268 hsgwqqz.lzc', 'dir wrmm'], 'dsmmcjtg': ['150156 lmtdgnll.bln', '192882 nzdgz.pzz'], 'cclw': ['245438 nzdgz.bdv'], 'fph': ['dir hztjntff', 'dir mbgv', 'dir nbzvd', 'dir tzjtsqlj', '313411 vwmsbfd.btp'], 'mbgv': ['890 zjnll.zjl'], 'nbzvd': ['95080 zvjf.zjq'], 'tzjtsqlj': ['224995 frcqrdm'], 'hvvvv': ['dir zrpvfzz'], 'zrpvfzz': ['dir nlcds', '280153 slcjdqw.wms'], 'nlcds': ['80960 cwsf.qtp'], 'fwmvqhj': ['dir cwsf', '209425 fcf.ncz', '139449 gllwzh.dzc', 'dir hjgpzwf', 'dir njtbnt'], 'hjgpzwf': ['157649 jcw'], 'njtbnt': ['dir lvhqrjzn', 'dir mgtjfhvf', '31491 nzdgz.sgc'], 'lvhqrjzn': ['11465 rrfpsjm.fsd'], 'mgtjfhvf': ['dir wmnwrn'], 'wmnwrn': ['44518 hwtj'], 'hnwn': ['265411 bftcf.hdj', 'dir bqg'], 'jgdjp': ['165322 vdpnqwq'], 'qzlt': ['44763 cwsf.qqz', 'dir jcgt', 'dir vmsnrhb', 'dir wrmm'], 'jcgt': ['199928 hnl.chj'], 'vmsnrhb': ['dir csvhwb', 'dir mnwwdf', 'dir pzwvh'], 'csvhwb': ['82347 bqg.qlb', '76688 dtl.nws', 'dir hztjntff', '151835 nwwdct.qlc', 'dir prqf'], 'prqf': ['143916 hcfv.jpr', '60506 hztjntff', '295807 jqwmltv.dmb', '282209 qmzpbn.ntn'], 'mnwwdf': ['161210 nzdgz.mjn'], 'pzwvh': ['28510 cwgtzgjd.ghf', 'dir jbhjjjs', 'dir lql', '25334 lsb', 'dir wcrsqtz'], 'jbhjjjs': ['48808 mhshl'], 'lql': ['dir tzcjpj'], 'tzcjpj': ['101686 frcqrdm'], 'wcrsqtz': ['71563 bqg.zmh', '270956 qgw', 'dir rngvpc'], 'rngvpc': ['220454 smfzwq.qgr'], 'mvrqsc': ['249653 frcqrdm', '257853 nzdgz.qbf'], 'tmzgrts': ['229931 djssmcdz.nzj', 'dir jrbjdghc', '131107 rjtsdjqt.mht'], 'jrbjdghc': ['85458 frcqrdm'], 'tqqqv': ['162333 bqg.mdz', '5054 hcfv.jpr', '172441 nzdgz', 'dir qmwpfp', '18969 wrmm'], 'qmwpfp': ['dir cwsf', 'dir lndh', 'dir nvjsvvln'], 'wlpcb': ['280918 vllc.ztt'], 'lndh': ['146958 lvsqcvlr.bcq', '286212 vcpgqbl.wbw'], 'nvjsvvln': ['288486 hcfv.jpr'], 'zmtmr': ['18654 cwsf.qpj', '89300 fprft.wbq', '66999 hwtj', '110810 lmtdjgpv', 'dir sms', 'dir vdn', 'dir vdqmtjw'], 'sms': ['85804 dtsgp', '197739 hcfv.jpr'], 'vdn': ['159126 tnmhfscw', '168030 wrmm.dvb'],
'vdqmtjw': ['291828 hztjntff'], 'wrmm': ['212937 frfrfr', '153487 ssss']} # make_system(data)
print()
print(f"result of make_system: {system_in_dict}")
print()

def sum_all_files(dictionary_system):
    dictionary_of_sums = {}
    for dir in dictionary_system:
        sum_of_sizes = 0
        list_of_content = []
        for file in dictionary_system[dir]:
            try:
                size_of_file = int(file.split()[0])
                sum_of_sizes += size_of_file
            except:
                list_of_content.append(file[4:])
        list_of_content.append(sum_of_sizes)
        if len(list_of_content) == 1:
            dictionary_of_sums[dir] = list_of_content[0]
        else:
            dictionary_of_sums[dir] = list_of_content
    return dictionary_of_sums


counted_files = sum_all_files(system_in_dict)       # good
print(f"sum_all_files: {counted_files}")


def separate_counted_folders(dict_with_all_files_counted):
    dictionary_result = {}
    for part in dict_with_all_files_counted:
        if isinstance(dict_with_all_files_counted[part], int):
            dictionary_result[part] = dict_with_all_files_counted[part]
    return dictionary_result


only_sizes = separate_counted_folders(counted_files)
#print(f"only sizes: {only_sizes}")


def iterate_list(some_list):
    for item in some_list:
        yield item


def reduce_known_dirs(dict_with_all_files_counted):
    new_dict = {}
    for part in dict_with_all_files_counted:
        content = dict_with_all_files_counted[part]
        try:
            new_dict[part] = sum(content)
        except:
            if isinstance(content, list):   #  and len(content) == 2
                new_content = []
                for each in content:
                    if isinstance(each, str):
                        try:        # maybe delete this
                            if isinstance(dict_with_all_files_counted[each], int):

                                new_content.append(dict_with_all_files_counted[each])
                            else:
                                new_content.append(each)

                        except:
                            new_content.append(each)
                    else:
                        new_content.append(each)
                new_dict[part] = new_content
            else:
                only_sizes[part] = content
                new_dict[part] = content
    return new_dict


print()


def finish_counting():
    _ = reduce_known_dirs(counted_files)
    while len(only_sizes) != len(_):

        _ = reduce_known_dirs(_)
    return only_sizes


counted_everything = finish_counting()

print(f"only sizes: {counted_everything}")


def separate_dirs_at_most_100000(finished_dict):
    cnt = 0
    for value in finished_dict:
        if finished_dict[value] < 100000:
            cnt += finished_dict[value]
    return cnt


print(f"final count: {separate_dirs_at_most_100000(counted_everything)}")


# last segment doesnt print out !!!!!! WTF? my dict