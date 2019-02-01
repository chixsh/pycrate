# -*- coding: UTF-8 -*-
# Code automatically generated by pycrate_asn1c

from pycrate_asn1rt.utils            import *
from pycrate_asn1rt.err              import *
from pycrate_asn1rt.glob             import make_GLOBAL, GLOBAL
from pycrate_asn1rt.dictobj          import ASN1Dict
from pycrate_asn1rt.refobj           import *
from pycrate_asn1rt.setobj           import *
from pycrate_asn1rt.asnobj_basic     import *
from pycrate_asn1rt.asnobj_str       import *
from pycrate_asn1rt.asnobj_construct import *
from pycrate_asn1rt.asnobj_class     import *
from pycrate_asn1rt.asnobj_ext       import *
from pycrate_asn1rt.init             import init_modules

class Test_Asn1rt:

    _name_  = u'Test-Asn1rt'
    _oid_   = []
    
    _obj_ = [
        u'Null',
        u'Boo01',
        u'Boo02',
        u'Int01',
        u'Int02',
        u'Int03',
        u'Int04',
        u'Int05',
        u'Int06',
        u'Int07',
        u'Int08',
        u'Int09',
        u'Int10',
        u'Int11',
        u'Int12',
        u'Int13',
        u'Int14',
        u'Rea01',
        u'Rea02',
        u'Enu01',
        u'Enu02',
        u'Enu03',
        u'Enu04',
        u'Oid01',
        u'Oid02',
        u'Bst01',
        u'Bst02',
        u'Bst03',
        u'Bst04',
        u'Bst05',
        u'Ost01',
        u'Ost02',
        u'Ost03',
        u'Ost04',
        u'Ost05',
        u'Nus01',
        u'Nus02',
        u'Prs01',
        u'Prs02',
        u'Ias01',
        u'Ias02',
        u'Ias03',
        u'U8s01',
        u'U8s02',
        u'U8s03',
        u'Uns01',
        u'Uns02',
        u'Uti01',
        u'Gti01',
        u'Int24',
        u'Cho01',
        u'Seq01',
        u'Seq02',
        u'Set01',
        ]
    _type_ = [
        u'Null',
        u'Boo01',
        u'Boo02',
        u'Int01',
        u'Int02',
        u'Int03',
        u'Int04',
        u'Int05',
        u'Int06',
        u'Int07',
        u'Int08',
        u'Int09',
        u'Int10',
        u'Int11',
        u'Int12',
        u'Int13',
        u'Int14',
        u'Rea01',
        u'Rea02',
        u'Enu01',
        u'Enu02',
        u'Enu03',
        u'Enu04',
        u'Oid01',
        u'Oid02',
        u'Bst01',
        u'Bst02',
        u'Bst03',
        u'Bst04',
        u'Bst05',
        u'Ost01',
        u'Ost02',
        u'Ost03',
        u'Ost04',
        u'Ost05',
        u'Nus01',
        u'Nus02',
        u'Prs01',
        u'Prs02',
        u'Ias01',
        u'Ias02',
        u'Ias03',
        u'U8s01',
        u'U8s02',
        u'U8s03',
        u'Uns01',
        u'Uns02',
        u'Uti01',
        u'Gti01',
        u'Int24',
        u'Cho01',
        u'Seq01',
        u'Seq02',
        u'Set01',
        ]
    _set_ = [
        ]
    _val_ = [
        ]
    _class_ = [
        ]
    _param_ = [
        ]
    
    #-----< Null >-----#
    Null = NULL(name=u'Null', mode=MODE_TYPE)
    
    #-----< Boo01 >-----#
    Boo01 = BOOL(name=u'Boo01', mode=MODE_TYPE)
    
    #-----< Boo02 >-----#
    Boo02 = BOOL(name=u'Boo02', mode=MODE_TYPE)
    Boo02._const_val = ASN1Set(rv=[True], rr=[], ev=None, er=[])
    
    #-----< Int01 >-----#
    Int01 = INT(name=u'Int01', mode=MODE_TYPE)
    
    #-----< Int02 >-----#
    Int02 = INT(name=u'Int02', mode=MODE_TYPE)
    Int02._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=None, ub=65535)], ev=None, er=[])
    
    #-----< Int03 >-----#
    Int03 = INT(name=u'Int03', mode=MODE_TYPE)
    Int03._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=-1, ub=None)], ev=None, er=[])
    
    #-----< Int04 >-----#
    Int04 = INT(name=u'Int04', mode=MODE_TYPE)
    Int04._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=1, ub=None)], ev=None, er=[])
    
    #-----< Int05 >-----#
    Int05 = INT(name=u'Int05', mode=MODE_TYPE)
    Int05._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=None)], ev=None, er=[])
    
    #-----< Int06 >-----#
    Int06 = INT(name=u'Int06', mode=MODE_TYPE)
    Int06._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=3, ub=6)], ev=None, er=[])
    
    #-----< Int07 >-----#
    Int07 = INT(name=u'Int07', mode=MODE_TYPE)
    Int07._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=4000, ub=4254)], ev=None, er=[])
    
    #-----< Int08 >-----#
    Int08 = INT(name=u'Int08', mode=MODE_TYPE)
    Int08._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=4000, ub=4255)], ev=None, er=[])
    
    #-----< Int09 >-----#
    Int09 = INT(name=u'Int09', mode=MODE_TYPE)
    Int09._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=32000)], ev=None, er=[])
    
    #-----< Int10 >-----#
    Int10 = INT(name=u'Int10', mode=MODE_TYPE)
    Int10._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=1, ub=65538)], ev=None, er=[])
    
    #-----< Int11 >-----#
    Int11 = INT(name=u'Int11', mode=MODE_TYPE)
    Int11._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=None, ub=65535)], ev=[], er=[])
    
    #-----< Int12 >-----#
    Int12 = INT(name=u'Int12', mode=MODE_TYPE)
    Int12._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=-1, ub=None)], ev=[], er=[])
    
    #-----< Int13 >-----#
    Int13 = INT(name=u'Int13', mode=MODE_TYPE)
    Int13._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=3, ub=6)], ev=[], er=[])
    
    #-----< Int14 >-----#
    Int14 = INT(name=u'Int14', mode=MODE_TYPE)
    Int14._const_val = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=1, ub=65538)], ev=[], er=[])
    
    #-----< Rea01 >-----#
    Rea01 = REAL(name=u'Rea01', mode=MODE_TYPE, typeref=ASN1RefType(('_IMPL_', 'REAL')))
    
    #-----< Rea02 >-----#
    Rea02 = REAL(name=u'Rea02', mode=MODE_TYPE, typeref=ASN1RefType(('_IMPL_', 'REAL')))
    Rea02._const_val = ASN1Set(rv=[], rr=[ASN1RangeReal(lb=(0, 10, -2), ub=(999, 10, -11), lb_incl=True, ub_incl=True)], ev=None, er=[])
    
    #-----< Enu01 >-----#
    Enu01 = ENUM(name=u'Enu01', mode=MODE_TYPE)
    Enu01._cont = ASN1Dict([(u'cheese', 0), (u'cake', 1), (u'coffee', 2), (u'tea', 3)])
    Enu01._ext = None
    
    #-----< Enu02 >-----#
    Enu02 = ENUM(name=u'Enu02', mode=MODE_TYPE)
    Enu02._cont = ASN1Dict([(u'cheese', 0)])
    Enu02._ext = None
    
    #-----< Enu03 >-----#
    Enu03 = ENUM(name=u'Enu03', mode=MODE_TYPE)
    Enu03._cont = ASN1Dict([(u'cheese', 0)])
    Enu03._ext = []
    
    #-----< Enu04 >-----#
    Enu04 = ENUM(name=u'Enu04', mode=MODE_TYPE)
    Enu04._cont = ASN1Dict([(u'cheese', 0), (u'cake', 1), (u'coffee', 2), (u'tea', 3)])
    Enu04._ext = [u'cake', u'coffee', u'tea']
    
    #-----< Oid01 >-----#
    Oid01 = OID(name=u'Oid01', mode=MODE_TYPE)
    
    #-----< Oid02 >-----#
    Oid02 = REL_OID(name=u'Oid02', mode=MODE_TYPE)
    
    #-----< Bst01 >-----#
    Bst01 = BIT_STR(name=u'Bst01', mode=MODE_TYPE)
    
    #-----< Bst02 >-----#
    Bst02 = BIT_STR(name=u'Bst02', mode=MODE_TYPE)
    Bst02._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=24)], ev=None, er=[])
    
    #-----< Bst03 >-----#
    Bst03 = BIT_STR(name=u'Bst03', mode=MODE_TYPE)
    Bst03._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=24)], ev=[], er=[])
    
    #-----< Bst04 >-----#
    Bst04 = BIT_STR(name=u'Bst04', mode=MODE_TYPE)
    Bst04._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=65536, ub=16777216)], ev=None, er=[])
    
    #-----< Bst05 >-----#
    Bst05 = BIT_STR(name=u'Bst05', mode=MODE_TYPE)
    _Bst05_contain = ENUM(name='_cont_Bst05', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Enu01')))
    Bst05._const_cont = _Bst05_contain
    
    #-----< Ost01 >-----#
    Ost01 = OCT_STR(name=u'Ost01', mode=MODE_TYPE)
    
    #-----< Ost02 >-----#
    Ost02 = OCT_STR(name=u'Ost02', mode=MODE_TYPE)
    Ost02._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=24)], ev=None, er=[])
    
    #-----< Ost03 >-----#
    Ost03 = OCT_STR(name=u'Ost03', mode=MODE_TYPE)
    Ost03._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=24)], ev=[], er=[])
    
    #-----< Ost04 >-----#
    Ost04 = OCT_STR(name=u'Ost04', mode=MODE_TYPE)
    Ost04._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=65536, ub=16777216)], ev=None, er=[])
    
    #-----< Ost05 >-----#
    Ost05 = OCT_STR(name=u'Ost05', mode=MODE_TYPE)
    _Ost05_contain = ENUM(name='_cont_Ost05', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Enu01')))
    Ost05._const_cont = _Ost05_contain
    
    #-----< Nus01 >-----#
    Nus01 = STR_NUM(name=u'Nus01', mode=MODE_TYPE)
    
    #-----< Nus02 >-----#
    Nus02 = STR_NUM(name=u'Nus02', mode=MODE_TYPE)
    Nus02._const_alpha = ASN1Set(rv=[u'0', u'1', u'2', u'3'], rr=[], ev=None, er=[])
    
    #-----< Prs01 >-----#
    Prs01 = STR_PRINT(name=u'Prs01', mode=MODE_TYPE)
    
    #-----< Prs02 >-----#
    Prs02 = STR_PRINT(name=u'Prs02', mode=MODE_TYPE)
    Prs02._const_alpha = ASN1Set(rv=[u'A', u'T', u'C', u'G'], rr=[], ev=None, er=[])
    
    #-----< Ias01 >-----#
    Ias01 = STR_IA5(name=u'Ias01', mode=MODE_TYPE)
    
    #-----< Ias02 >-----#
    Ias02 = STR_IA5(name=u'Ias02', mode=MODE_TYPE)
    Ias02._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=24)], ev=None, er=[])
    
    #-----< Ias03 >-----#
    Ias03 = STR_IA5(name=u'Ias03', mode=MODE_TYPE)
    Ias03._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=65535)], ev=[], er=[])
    
    #-----< U8s01 >-----#
    U8s01 = STR_UTF8(name=u'U8s01', mode=MODE_TYPE)
    
    #-----< U8s02 >-----#
    U8s02 = STR_UTF8(name=u'U8s02', mode=MODE_TYPE)
    U8s02._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=24)], ev=None, er=[])
    
    #-----< U8s03 >-----#
    U8s03 = STR_UTF8(name=u'U8s03', mode=MODE_TYPE)
    U8s03._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=65535)], ev=[], er=[])
    
    #-----< Uns01 >-----#
    Uns01 = STR_UNIV(name=u'Uns01', mode=MODE_TYPE)
    
    #-----< Uns02 >-----#
    Uns02 = STR_UNIV(name=u'Uns02', mode=MODE_TYPE)
    Uns02._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=0, ub=255)], ev=[], er=[])
    
    #-----< Uti01 >-----#
    Uti01 = TIME_UTC(name=u'Uti01', mode=MODE_TYPE)
    
    #-----< Gti01 >-----#
    Gti01 = TIME_GEN(name=u'Gti01', mode=MODE_TYPE)
    
    #-----< Int24 >-----#
    Int24 = INT(name=u'Int24', mode=MODE_TYPE, tag=(80, TAG_APPLICATION, TAG_EXPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Int04')))
    
    #-----< Cho01 >-----#
    Cho01 = CHOICE(name=u'Cho01', mode=MODE_TYPE)
    _Cho01_boo = BOOL(name=u'boo', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Boo01')))
    _Cho01_int = INT(name=u'int', mode=MODE_TYPE, tag=(10, TAG_CONTEXT_SPEC, TAG_EXPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Int24')))
    _Cho01_enu = ENUM(name=u'enu', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Enu01')))
    _Cho01_bst = BIT_STR(name=u'bst', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Bst03')))
    Cho01._cont = ASN1Dict([
        (u'boo', _Cho01_boo),
        (u'int', _Cho01_int),
        (u'enu', _Cho01_enu),
        (u'bst', _Cho01_bst),
        ])
    Cho01._ext = [u'bst']
    
    #-----< Seq01 >-----#
    Seq01 = SEQ(name=u'Seq01', mode=MODE_TYPE)
    _Seq01_boo = BOOL(name=u'boo', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Boo01')))
    _Seq01_int = INT(name=u'int', mode=MODE_TYPE, tag=(128, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Int24')), default=10)
    _Seq01_enu = ENUM(name=u'enu', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Enu01')), opt=True)
    _Seq01_bst = BIT_STR(name=u'bst', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Bst01')), group=0)
    _Seq01_ost = OCT_STR(name=u'ost', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Ost02')), group=0)
    Seq01._cont = ASN1Dict([
        (u'boo', _Seq01_boo),
        (u'int', _Seq01_int),
        (u'enu', _Seq01_enu),
        (u'bst', _Seq01_bst),
        (u'ost', _Seq01_ost),
        ])
    Seq01._ext = [u'bst', u'ost']
    
    #-----< Seq02 >-----#
    Seq02 = SEQ_OF(name=u'Seq02', mode=MODE_TYPE)
    _Seq02__item_ = STR_IA5(name='_item_', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Ias02')))
    Seq02._cont = _Seq02__item_
    Seq02._const_sz = ASN1Set(rv=[], rr=[ASN1RangeInt(lb=2, ub=5)], ev=None, er=[])
    
    #-----< Set01 >-----#
    Set01 = SET(name=u'Set01', mode=MODE_TYPE)
    _Set01_boo = BOOL(name=u'boo', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Boo01')))
    _Set01_int = INT(name=u'int', mode=MODE_TYPE, tag=(64, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Int04')), default=10)
    _Set01_cho = CHOICE(name=u'cho', mode=MODE_TYPE)
    __Set01_cho_boo = BOOL(name=u'boo', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Boo01')))
    __Set01_cho_int = INT(name=u'int', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Int04')))
    __Set01_cho_enu = ENUM(name=u'enu', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_IMPLICIT), typeref=ASN1RefType(('Test-Asn1rt', 'Enu01')))
    _Set01_cho._cont = ASN1Dict([
        (u'boo', __Set01_cho_boo),
        (u'int', __Set01_cho_int),
        (u'enu', __Set01_cho_enu),
        ])
    _Set01_cho._ext = None
    _Set01_enu = ENUM(name=u'enu', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Enu01')), opt=True)
    _Set01_bst = BIT_STR(name=u'bst', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Bst01')), group=0)
    _Set01_ost = OCT_STR(name=u'ost', mode=MODE_TYPE, typeref=ASN1RefType(('Test-Asn1rt', 'Ost02')), group=0)
    Set01._cont = ASN1Dict([
        (u'boo', _Set01_boo),
        (u'int', _Set01_int),
        (u'cho', _Set01_cho),
        (u'enu', _Set01_enu),
        (u'bst', _Set01_bst),
        (u'ost', _Set01_ost),
        ])
    Set01._ext = [u'bst', u'ost']
    
    _all_ = [
        Null,
        Boo01,
        Boo02,
        Int01,
        Int02,
        Int03,
        Int04,
        Int05,
        Int06,
        Int07,
        Int08,
        Int09,
        Int10,
        Int11,
        Int12,
        Int13,
        Int14,
        Rea01,
        Rea02,
        Enu01,
        Enu02,
        Enu03,
        Enu04,
        Oid01,
        Oid02,
        Bst01,
        Bst02,
        Bst03,
        Bst04,
        _Bst05_contain,
        Bst05,
        Ost01,
        Ost02,
        Ost03,
        Ost04,
        _Ost05_contain,
        Ost05,
        Nus01,
        Nus02,
        Prs01,
        Prs02,
        Ias01,
        Ias02,
        Ias03,
        U8s01,
        U8s02,
        U8s03,
        Uns01,
        Uns02,
        Uti01,
        Gti01,
        Int24,
        _Cho01_boo,
        _Cho01_int,
        _Cho01_enu,
        _Cho01_bst,
        Cho01,
        _Seq01_boo,
        _Seq01_int,
        _Seq01_enu,
        _Seq01_bst,
        _Seq01_ost,
        Seq01,
        _Seq02__item_,
        Seq02,
        _Set01_boo,
        _Set01_int,
        __Set01_cho_boo,
        __Set01_cho_int,
        __Set01_cho_enu,
        _Set01_cho,
        _Set01_enu,
        _Set01_bst,
        _Set01_ost,
        Set01,
    ]

class _IMPL_:

    _name_ = '_IMPL_'
    _oid_  = []
    _obj_  = ['REAL', 'EXTERNAL', 'EMBEDDED PDV', 'CHARACTER STRING', 'TYPE-IDENTIFIER', 'ABSTRACT-SYNTAX']
    
    #-----< REAL >-----#
    REAL = SEQ(name='REAL', mode=MODE_TYPE)
    _REAL_mantissa = INT(name='mantissa', mode=MODE_TYPE)
    _REAL_base = INT(name='base', mode=MODE_TYPE)
    _REAL_base._const_val = ASN1Set(rv=[2, 10], rr=[], ev=None, er=[])
    _REAL_exponent = INT(name='exponent', mode=MODE_TYPE)
    REAL._cont = ASN1Dict([
        ('mantissa', _REAL_mantissa),
        ('base', _REAL_base),
        ('exponent', _REAL_exponent),
        ])
    REAL._ext = None
    
    #-----< EXTERNAL >-----#
    EXTERNAL = SEQ(name='EXTERNAL', mode=MODE_TYPE)
    _EXTERNAL_identification = CHOICE(name='identification', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EXTERNAL_identification_syntaxes = SEQ(name='syntaxes', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EXTERNAL_identification_syntaxes_abstract = OID(name='abstract', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EXTERNAL_identification_syntaxes_transfer = OID(name='transfer', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EXTERNAL_identification_syntaxes._cont = ASN1Dict([
        ('abstract', ___EXTERNAL_identification_syntaxes_abstract),
        ('transfer', ___EXTERNAL_identification_syntaxes_transfer),
        ])
    __EXTERNAL_identification_syntaxes._ext = None
    __EXTERNAL_identification_syntax = OID(name='syntax', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EXTERNAL_identification_presentation_context_id = INT(name='presentation-context-id', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EXTERNAL_identification_context_negotiation = SEQ(name='context-negotiation', mode=MODE_TYPE, tag=(3, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EXTERNAL_identification_context_negotiation_presentation_context_id = INT(name='presentation-context-id', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EXTERNAL_identification_context_negotiation_transfer_syntax = OID(name='transfer-syntax', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EXTERNAL_identification_context_negotiation._cont = ASN1Dict([
        ('presentation-context-id', ___EXTERNAL_identification_context_negotiation_presentation_context_id),
        ('transfer-syntax', ___EXTERNAL_identification_context_negotiation_transfer_syntax),
        ])
    __EXTERNAL_identification_context_negotiation._ext = None
    __EXTERNAL_identification_transfer_syntax = OID(name='transfer-syntax', mode=MODE_TYPE, tag=(4, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EXTERNAL_identification_fixed = NULL(name='fixed', mode=MODE_TYPE, tag=(5, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    _EXTERNAL_identification._cont = ASN1Dict([
        ('syntaxes', __EXTERNAL_identification_syntaxes),
        ('syntax', __EXTERNAL_identification_syntax),
        ('presentation-context-id', __EXTERNAL_identification_presentation_context_id),
        ('context-negotiation', __EXTERNAL_identification_context_negotiation),
        ('transfer-syntax', __EXTERNAL_identification_transfer_syntax),
        ('fixed', __EXTERNAL_identification_fixed),
        ])
    _EXTERNAL_identification._ext = None
    _EXTERNAL_data_value_descriptor = OBJ_DESC(name='data-value-descriptor', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT), opt=True)
    _EXTERNAL_data_value = OCT_STR(name='data-value', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    EXTERNAL._cont = ASN1Dict([
        ('identification', _EXTERNAL_identification),
        ('data-value-descriptor', _EXTERNAL_data_value_descriptor),
        ('data-value', _EXTERNAL_data_value),
        ])
    EXTERNAL._ext = None
    
    #-----< EMBEDDED PDV >-----#
    EMBEDDED_PDV = SEQ(name='EMBEDDED PDV', mode=MODE_TYPE)
    _EMBEDDED_PDV_identification = CHOICE(name='identification', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EMBEDDED_PDV_identification_syntaxes = SEQ(name='syntaxes', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EMBEDDED_PDV_identification_syntaxes_abstract = OID(name='abstract', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EMBEDDED_PDV_identification_syntaxes_transfer = OID(name='transfer', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EMBEDDED_PDV_identification_syntaxes._cont = ASN1Dict([
        ('abstract', ___EMBEDDED_PDV_identification_syntaxes_abstract),
        ('transfer', ___EMBEDDED_PDV_identification_syntaxes_transfer),
        ])
    __EMBEDDED_PDV_identification_syntaxes._ext = None
    __EMBEDDED_PDV_identification_syntax = OID(name='syntax', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EMBEDDED_PDV_identification_presentation_context_id = INT(name='presentation-context-id', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EMBEDDED_PDV_identification_context_negotiation = SEQ(name='context-negotiation', mode=MODE_TYPE, tag=(3, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EMBEDDED_PDV_identification_context_negotiation_presentation_context_id = INT(name='presentation-context-id', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___EMBEDDED_PDV_identification_context_negotiation_transfer_syntax = OID(name='transfer-syntax', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EMBEDDED_PDV_identification_context_negotiation._cont = ASN1Dict([
        ('presentation-context-id', ___EMBEDDED_PDV_identification_context_negotiation_presentation_context_id),
        ('transfer-syntax', ___EMBEDDED_PDV_identification_context_negotiation_transfer_syntax),
        ])
    __EMBEDDED_PDV_identification_context_negotiation._ext = None
    __EMBEDDED_PDV_identification_transfer_syntax = OID(name='transfer-syntax', mode=MODE_TYPE, tag=(4, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __EMBEDDED_PDV_identification_fixed = NULL(name='fixed', mode=MODE_TYPE, tag=(5, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    _EMBEDDED_PDV_identification._cont = ASN1Dict([
        ('syntaxes', __EMBEDDED_PDV_identification_syntaxes),
        ('syntax', __EMBEDDED_PDV_identification_syntax),
        ('presentation-context-id', __EMBEDDED_PDV_identification_presentation_context_id),
        ('context-negotiation', __EMBEDDED_PDV_identification_context_negotiation),
        ('transfer-syntax', __EMBEDDED_PDV_identification_transfer_syntax),
        ('fixed', __EMBEDDED_PDV_identification_fixed),
        ])
    _EMBEDDED_PDV_identification._ext = None
    _EMBEDDED_PDV_data_value_descriptor = OBJ_DESC(name='data-value-descriptor', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT), opt=True)
    _EMBEDDED_PDV_data_value = OCT_STR(name='data-value', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    EMBEDDED_PDV._cont = ASN1Dict([
        ('identification', _EMBEDDED_PDV_identification),
        ('data-value-descriptor', _EMBEDDED_PDV_data_value_descriptor),
        ('data-value', _EMBEDDED_PDV_data_value),
        ])
    EMBEDDED_PDV._ext = None
    
    #-----< CHARACTER STRING >-----#
    CHARACTER_STRING = SEQ(name='CHARACTER STRING', mode=MODE_TYPE)
    _CHARACTER_STRING_identification = CHOICE(name='identification', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __CHARACTER_STRING_identification_syntaxes = SEQ(name='syntaxes', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___CHARACTER_STRING_identification_syntaxes_abstract = OID(name='abstract', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___CHARACTER_STRING_identification_syntaxes_transfer = OID(name='transfer', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __CHARACTER_STRING_identification_syntaxes._cont = ASN1Dict([
        ('abstract', ___CHARACTER_STRING_identification_syntaxes_abstract),
        ('transfer', ___CHARACTER_STRING_identification_syntaxes_transfer),
        ])
    __CHARACTER_STRING_identification_syntaxes._ext = None
    __CHARACTER_STRING_identification_syntax = OID(name='syntax', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __CHARACTER_STRING_identification_presentation_context_id = INT(name='presentation-context-id', mode=MODE_TYPE, tag=(2, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __CHARACTER_STRING_identification_context_negotiation = SEQ(name='context-negotiation', mode=MODE_TYPE, tag=(3, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___CHARACTER_STRING_identification_context_negotiation_presentation_context_id = INT(name='presentation-context-id', mode=MODE_TYPE, tag=(0, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    ___CHARACTER_STRING_identification_context_negotiation_transfer_syntax = OID(name='transfer-syntax', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __CHARACTER_STRING_identification_context_negotiation._cont = ASN1Dict([
        ('presentation-context-id', ___CHARACTER_STRING_identification_context_negotiation_presentation_context_id),
        ('transfer-syntax', ___CHARACTER_STRING_identification_context_negotiation_transfer_syntax),
        ])
    __CHARACTER_STRING_identification_context_negotiation._ext = None
    __CHARACTER_STRING_identification_transfer_syntax = OID(name='transfer-syntax', mode=MODE_TYPE, tag=(4, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    __CHARACTER_STRING_identification_fixed = NULL(name='fixed', mode=MODE_TYPE, tag=(5, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    _CHARACTER_STRING_identification._cont = ASN1Dict([
        ('syntaxes', __CHARACTER_STRING_identification_syntaxes),
        ('syntax', __CHARACTER_STRING_identification_syntax),
        ('presentation-context-id', __CHARACTER_STRING_identification_presentation_context_id),
        ('context-negotiation', __CHARACTER_STRING_identification_context_negotiation),
        ('transfer-syntax', __CHARACTER_STRING_identification_transfer_syntax),
        ('fixed', __CHARACTER_STRING_identification_fixed),
        ])
    _CHARACTER_STRING_identification._ext = None
    _CHARACTER_STRING_string_value = OCT_STR(name='string-value', mode=MODE_TYPE, tag=(1, TAG_CONTEXT_SPEC, TAG_EXPLICIT))
    CHARACTER_STRING._cont = ASN1Dict([
        ('identification', _CHARACTER_STRING_identification),
        ('string-value', _CHARACTER_STRING_string_value),
        ])
    CHARACTER_STRING._ext = None
    
    #-----< TYPE-IDENTIFIER >-----#
    TYPE_IDENTIFIER = CLASS(name='TYPE-IDENTIFIER', mode=MODE_TYPE)
    _TYPE_IDENTIFIER_id = OID(name='id', mode=MODE_VALUE, uniq=True)
    _TYPE_IDENTIFIER_Type = OPEN(name='Type', mode=MODE_TYPE)
    TYPE_IDENTIFIER._cont = ASN1Dict([
        ('id', _TYPE_IDENTIFIER_id),
        ('Type', _TYPE_IDENTIFIER_Type),
        ])
    
    #-----< ABSTRACT-SYNTAX >-----#
    ABSTRACT_SYNTAX = CLASS(name='ABSTRACT-SYNTAX', mode=MODE_TYPE)
    _ABSTRACT_SYNTAX_id = OID(name='id', mode=MODE_VALUE)
    _ABSTRACT_SYNTAX_Type = OPEN(name='Type', mode=MODE_TYPE)
    _ABSTRACT_SYNTAX_property = BIT_STR(name='property', mode=MODE_VALUE, default=(0, 0))
    _ABSTRACT_SYNTAX_property._cont = ASN1Dict([('handles-invalid-encodings', 0)])
    ABSTRACT_SYNTAX._cont = ASN1Dict([
        ('id', _ABSTRACT_SYNTAX_id),
        ('Type', _ABSTRACT_SYNTAX_Type),
        ('property', _ABSTRACT_SYNTAX_property),
        ])
    
    _all_ = [
        _REAL_mantissa,
        _REAL_base,
        _REAL_exponent,
        REAL,
        ___EXTERNAL_identification_syntaxes_abstract,
        ___EXTERNAL_identification_syntaxes_transfer,
        __EXTERNAL_identification_syntaxes,
        __EXTERNAL_identification_syntax,
        __EXTERNAL_identification_presentation_context_id,
        ___EXTERNAL_identification_context_negotiation_presentation_context_id,
        ___EXTERNAL_identification_context_negotiation_transfer_syntax,
        __EXTERNAL_identification_context_negotiation,
        __EXTERNAL_identification_transfer_syntax,
        __EXTERNAL_identification_fixed,
        _EXTERNAL_identification,
        _EXTERNAL_data_value_descriptor,
        _EXTERNAL_data_value,
        EXTERNAL,
        ___EMBEDDED_PDV_identification_syntaxes_abstract,
        ___EMBEDDED_PDV_identification_syntaxes_transfer,
        __EMBEDDED_PDV_identification_syntaxes,
        __EMBEDDED_PDV_identification_syntax,
        __EMBEDDED_PDV_identification_presentation_context_id,
        ___EMBEDDED_PDV_identification_context_negotiation_presentation_context_id,
        ___EMBEDDED_PDV_identification_context_negotiation_transfer_syntax,
        __EMBEDDED_PDV_identification_context_negotiation,
        __EMBEDDED_PDV_identification_transfer_syntax,
        __EMBEDDED_PDV_identification_fixed,
        _EMBEDDED_PDV_identification,
        _EMBEDDED_PDV_data_value_descriptor,
        _EMBEDDED_PDV_data_value,
        EMBEDDED_PDV,
        ___CHARACTER_STRING_identification_syntaxes_abstract,
        ___CHARACTER_STRING_identification_syntaxes_transfer,
        __CHARACTER_STRING_identification_syntaxes,
        __CHARACTER_STRING_identification_syntax,
        __CHARACTER_STRING_identification_presentation_context_id,
        ___CHARACTER_STRING_identification_context_negotiation_presentation_context_id,
        ___CHARACTER_STRING_identification_context_negotiation_transfer_syntax,
        __CHARACTER_STRING_identification_context_negotiation,
        __CHARACTER_STRING_identification_transfer_syntax,
        __CHARACTER_STRING_identification_fixed,
        _CHARACTER_STRING_identification,
        _CHARACTER_STRING_string_value,
        CHARACTER_STRING,
        _TYPE_IDENTIFIER_id,
        _TYPE_IDENTIFIER_Type,
        TYPE_IDENTIFIER,
        _ABSTRACT_SYNTAX_id,
        _ABSTRACT_SYNTAX_Type,
        _ABSTRACT_SYNTAX_property,
        ABSTRACT_SYNTAX,
    ]

init_modules(Test_Asn1rt, _IMPL_)
