<!DOCTYPE html>
<!-- saved from url=(0106)https://colab.research.google.com/drive/1ePorOpCgRwO3hvAjOLVd-PUSZpysM-wW?authuser=1#scrollTo=EdN6CbYFl6HE -->
<html lang="fr" theme="adaptive" editor="Default Light"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><meta http-equiv="origin-trial" content="A/kargTFyk8MR5ueravczef/wIlTkbVk1qXQesp39nV+xNECPdLBVeYffxrM8TmZT6RArWGQVCJ0LRivD7glcAUAAACQeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTksImlzU3ViZG9tYWluIjp0cnVlLCJpc1RoaXJkUGFydHkiOnRydWV9"><script type="text/javascript" async="" charset="utf-8" src="./Analyse de données_files/recaptcha__fr.js.télécharger" crossorigin="anonymous" integrity="sha384-RKRU1+0SoaCK7t7YnwipRCwDQ6Lq/KhGzlZr2vG2V8rORxpYnoXBbmonrM7F9iv4" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./Analyse de données_files/recaptcha__fr.js.télécharger" crossorigin="anonymous" integrity="sha384-RKRU1+0SoaCK7t7YnwipRCwDQ6Lq/KhGzlZr2vG2V8rORxpYnoXBbmonrM7F9iv4" nonce=""></script><script type="text/javascript" async="" src="./Analyse de données_files/js" nonce=""></script><script src="./Analyse de données_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./Analyse de données_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./Analyse de données_files/analytics.js.télécharger"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Analyse_de_données.ipynb - Colab</title><link href="./Analyse de données_files/css2" rel="stylesheet"><link href="./Analyse de données_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_2d:not(.gb_pe){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Pa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Pa:hover::after,a.gb_Pa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Pa:hover,a.gb_Pa:focus{text-decoration:none}a.gb_Pa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Qa{background-color:#4285f4;color:#fff}a.gb_Qa:active{background-color:#0043b2}.gb_Ra{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Pa,.gb_Qa,.gb_Sa,.gb_Ta{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Sa{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ta{background:#f8f8f8}.gb_Sa,#gb a.gb_Sa.gb_Sa,.gb_Ta{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ta{cursor:default;text-decoration:none}.gb_Ta{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ta{color:#fff}.gb_Ta:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ta:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Ua{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Ua:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Ua:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Ua:active,#gb .gb_Ua:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Ua.gb_F{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Ua.gb_F:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Ua.gb_F:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Ua.gb_F:active,#gb .gb_Ua.gb_F:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_bd{display:inline-block;vertical-align:middle}.gb_Oe .gb_P{bottom:-3px;right:-5px}.gb_C{position:relative}.gb_A{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_A{cursor:pointer;text-decoration:none}.gb_A,a.gb_A{color:#000}.gb_cd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_dd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_dd{border-bottom-color:#ccc}.gb_ka{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_bd.gb_Sc .gb_cd,.gb_bd.gb_Sc .gb_dd,.gb_bd.gb_Sc .gb_ka,.gb_Sc.gb_ka{display:block}.gb_bd.gb_Sc.gb_ed .gb_cd,.gb_bd.gb_Sc.gb_ed .gb_dd{display:none}.gb_Pe{position:absolute;right:8px;top:62px;z-index:-1}.gb_fd .gb_cd,.gb_fd .gb_dd,.gb_fd .gb_ka{margin-top:-10px}.gb_bd:first-child,#gbsfw:first-child+.gb_bd{padding-left:4px}.gb_Ea.gb_Qe .gb_bd:first-child{padding-left:0}.gb_Re{position:relative}.gb_1c .gb_Re,.gb_Id .gb_Re{float:right}.gb_A{padding:8px;cursor:pointer}.gb_A::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Ea .gb_gd:not(.gb_Pa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_hd button svg,.gb_A{-webkit-border-radius:50%;border-radius:50%}.gb_hd button:focus:not(:focus-visible) svg,.gb_hd button:hover svg,.gb_hd button:active svg,.gb_A:focus:not(:focus-visible),.gb_A:hover,.gb_A:active,.gb_A[aria-expanded=true]{outline:none}.gb_Kc .gb_hd.gb_id button:focus-visible svg,.gb_hd button:focus-visible svg,.gb_A:focus-visible{outline:1px solid #202124}.gb_Kc .gb_hd button:focus-visible svg,.gb_Kc .gb_A:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Kc .gb_hd.gb_id button:focus-visible svg,.gb_hd button:focus-visible svg,.gb_Kc .gb_hd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Kc .gb_hd.gb_id button:focus svg,.gb_Kc .gb_hd.gb_id button:focus:hover svg,.gb_hd button:focus svg,.gb_hd button:focus:hover svg,.gb_A:focus,.gb_A:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Kc .gb_hd.gb_id button:active svg,.gb_hd button:active svg,.gb_A:active{background-color:rgba(60,64,67,.12)}.gb_Kc .gb_hd.gb_id button:hover svg,.gb_hd button:hover svg,.gb_A:hover{background-color:rgba(60,64,67,.08)}.gb_Va .gb_A.gb_Xa:hover{background-color:transparent}.gb_A[aria-expanded=true],.gb_A:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_A[aria-expanded=true] .gb_E{fill:#5f6368;opacity:1}.gb_Kc .gb_hd button:hover svg,.gb_Kc .gb_A:hover{background-color:rgba(232,234,237,.08)}.gb_Kc .gb_hd button:focus svg,.gb_Kc .gb_hd button:focus:hover svg,.gb_Kc .gb_A:focus,.gb_Kc .gb_A:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Kc .gb_hd button:active svg,.gb_Kc .gb_A:active{background-color:rgba(232,234,237,.12)}.gb_Kc .gb_A[aria-expanded=true],.gb_Kc .gb_A:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Kc .gb_A[aria-expanded=true] .gb_E{fill:#fff;opacity:1}.gb_bd{padding:4px}.gb_Ea.gb_Qe .gb_bd{padding:4px 2px}.gb_Ea.gb_Qe .gb_y.gb_bd{padding-left:6px}.gb_ka{z-index:991;line-height:normal}.gb_ka.gb_jd{left:0;right:auto}@media (max-width:350px){.gb_ka.gb_jd{left:0}}.gb_Se .gb_ka{top:56px}.gb_Q{display:none!important}.gb_md{visibility:hidden}.gb_I .gb_A,.gb_ja .gb_I .gb_A{background-position:-64px -29px}.gb_0 .gb_I .gb_A{background-position:-29px -29px;opacity:1}.gb_I .gb_A,.gb_I .gb_A:hover,.gb_I .gb_A:focus{opacity:1}.gb_K{display:none}@media screen and (max-width:319px){.gb_kd:not(.gb_ld) .gb_I{display:none;visibility:hidden}}.gb_P{display:none}.gb_8c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_8c.gb_9c{color:#3c4043}.gb_Ea.gb_bc .gb_8c{margin-bottom:0}.gb_rd.gb_td .gb_8c{padding-left:4px}.gb_Ea.gb_bc .gb_ud{position:relative;top:-2px}.gb_ad{display:none}.gb_Ea{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Ea.gb_Rc{min-width:120px}.gb_Ea.gb_vd .gb_wd{display:none}.gb_Ea.gb_vd .gb_kd{height:56px}header.gb_Ea{display:block}.gb_Ea svg{fill:currentColor}.gb_Cd{position:fixed;top:0;width:100%}.gb_xd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Dd{height:64px}.gb_kd{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ea:not(.gb_bc) .gb_kd{padding:8px}.gb_Ea.gb_Ed .gb_kd{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Ea .gb_kd.gb_ld.gb_Fd{min-width:0}.gb_Ea.gb_bc .gb_kd{padding:4px;padding-left:8px;min-width:0}.gb_wd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_zd>.gb_wd{display:table-cell;width:100%}.gb_rd{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Ea.gb_bc .gb_rd{padding-right:14px}.gb_Ad{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Ad>:only-child{display:inline-block}.gb_Bd.gb_2c{padding-left:4px}.gb_Bd.gb_Hd,.gb_Ea.gb_Ed .gb_Bd,.gb_Ea.gb_bc:not(.gb_Id) .gb_Bd{padding-left:0}.gb_Ea.gb_bc .gb_Bd.gb_Hd{padding-right:0}.gb_Ea.gb_bc .gb_Bd.gb_Hd .gb_Va{margin-left:10px}.gb_2c{display:inline}.gb_Ea.gb_Vc .gb_Bd.gb_Jd,.gb_Ea.gb_Id .gb_Bd.gb_Jd{padding-left:2px}.gb_8c{display:inline-block}.gb_Bd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Id{height:48px}.gb_Ea.gb_Id{min-width:auto}.gb_Id .gb_Bd{float:right;padding-left:32px}.gb_Id .gb_Bd.gb_Kd{padding-left:0}.gb_Ld{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_od{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Md{color:black}.gb_Kc{color:white}.gb_Ea a,.gb_Oc a{color:inherit}.gb_aa{color:rgba(0,0,0,.87)}.gb_Ea svg,.gb_Oc svg,.gb_rd .gb_sd,.gb_1c .gb_sd{color:#5f6368;opacity:1}.gb_Kc svg,.gb_Oc.gb_Tc svg,.gb_Kc .gb_rd .gb_sd,.gb_Kc .gb_rd .gb_Jc,.gb_Kc .gb_rd .gb_ud,.gb_Oc.gb_Tc .gb_sd{color:rgba(255,255,255,.87)}.gb_Kc .gb_rd .gb_Nd:not(.gb_Od){opacity:.87}.gb_9c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Kc .gb_9c,.gb_Md .gb_9c{opacity:1}.gb_Pd{position:relative}.gb_L{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_W,span.gb_W{color:rgba(0,0,0,.87);text-decoration:none}.gb_Kc a.gb_W,.gb_Kc span.gb_W{color:white}a.gb_W:focus{outline-offset:2px}a.gb_W:hover{text-decoration:underline}.gb_X{display:inline-block;padding-left:15px}.gb_X .gb_W{display:inline-block;line-height:24px;vertical-align:middle}.gb_pd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Ea.gb_Id .gb_pd{margin-left:8px}#gb a.gb_Ta.gb_pd{cursor:pointer}.gb_Ta.gb_pd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ta.gb_pd:focus,.gb_Ta.gb_pd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ta.gb_pd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_pd{background:#1a73e8;border:1px solid transparent}.gb_Ea.gb_bc .gb_pd{padding:9px 15px;min-width:80px}.gb_Qd{text-align:left}#gb .gb_Kc a.gb_pd:not(.gb_F),#gb.gb_Kc a.gb_pd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ta.gb_F.gb_pd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Kc a.gb_pd:hover:not(.gb_F),#gb.gb_Kc a.gb_pd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ta.gb_F.gb_pd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Kc a.gb_pd:focus:not(.gb_F),#gb .gb_Kc a.gb_pd:focus:hover:not(.gb_F),#gb.gb_Kc a.gb_pd:focus:not(.gb_F),#gb.gb_Kc a.gb_pd:focus:hover:not(.gb_F){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ta.gb_F.gb_pd:focus,#gb a.gb_Ta.gb_F.gb_pd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Kc a.gb_pd:active:not(.gb_F),#gb.gb_Kc a.gb_pd:active{background:#ecf3fe}#gb a.gb_Ta.gb_F.gb_pd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_J{display:none}@media screen and (max-width:319px){.gb_kd .gb_I{display:none;visibility:hidden}}.gb_Va{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Va.gb_F{background-color:transparent;border:1px solid #5f6368}.gb_2a{display:inherit}.gb_Va.gb_F .gb_2a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Va:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Va.gb_F:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Va:focus-visible,.gb_Va:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Va.gb_F:focus-visible,.gb_Va.gb_F:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Va.gb_F:active,.gb_Va.gb_Sc.gb_F:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_3a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Va.gb_F .gb_3a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_3a.gb_4a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_3a.gb_4a .gb_Hc{vertical-align:middle}.gb_Ea:not(.gb_bc) .gb_Va{margin-left:10px;margin-right:4px}.gb_Rd{max-height:32px;width:78px}.gb_Va.gb_F .gb_Rd{max-height:26px;width:72px}.gb_O{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_db{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_db.gb_O{height:30px;width:30px}.gb_db.gb_O:hover,.gb_db.gb_O:active{-webkit-box-shadow:none;box-shadow:none}.gb_eb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_vc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_O::before,.gb_fb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_2 .gb_fb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_O:hover,.gb_O:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_O:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_O:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_gb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_A.gb_gb{width:auto}.gb_gb:hover,.gb_gb:focus{opacity:.85}.gb_fd .gb_gb,.gb_fd .gb_Ud{line-height:26px}#gb#gb.gb_fd a.gb_gb,.gb_fd .gb_Ud{font-size:11px;height:auto}.gb_hb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Xa:hover .gb_hb{opacity:.85}.gb_Va>.gb_y{padding:3px 3px 3px 4px}.gb_Vd.gb_md{color:#fff}.gb_0 .gb_gb,.gb_0 .gb_hb{opacity:1}#gb#gb.gb_0.gb_0 a.gb_gb,#gb#gb .gb_0.gb_0 a.gb_gb{color:#fff}.gb_0.gb_0 .gb_hb{border-top-color:#fff;opacity:1}.gb_ja .gb_O:hover,.gb_0 .gb_O:hover,.gb_ja .gb_O:focus,.gb_0 .gb_O:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Wd .gb_y,.gb_Xd .gb_y{position:absolute;right:1px}.gb_y.gb_Z,.gb_ib.gb_Z,.gb_Xa.gb_Z{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_Zd.gb_0d .gb_gb{width:30px!important}.gb_1d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_2d .gb_1d,.gb_3d .gb_1d{right:0;top:0}.gb_y .gb_A{padding:4px}.gb_R{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.Z8FBMQoacoc.2019.O","tn","fr","425",0,[4,2,"","","","699802849","0"],null,"yoJPZ77cCr7Np84PstOhoQU",null,0,"og.qtm.zyyRgCCaN80.L.W.O","AA2YrTt16WS-AyvNEln9-TaO-tZR_15utQ","AA2YrTs4SLbgh5FvGZPW_Ny7TyTdXfy6xA","",2,1,200,"TUN",null,null,"425","425",1,null,null,114591953,1,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"1","rimahben0@gmail.com","","ADxTByr7jEFDqz-S3JlxJlfVJzDd7VqgHq4rOTfHw5S9vPao03VGzs_tZ6MrCNKmtYrDrh1yB5_Qfcxc38584OMn-5ZggKfX5A",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (par défaut)","Compte de marque",1,"%1$s (délégué)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=1\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=fr\u0026ts=250",0,"dashboard",null,null,null,null,"Profil","",1,null,"Déconnecté","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Supprimer","Se connecter",0,1,1,0,1,1,0,null,null,null,"Session arrivée à expiration",null,null,null,"Visiteur",null,"Par défaut","Délégué","Se déconnecter de tous les comptes",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","1","fr"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.x7CxCIZpks8.O/am=AAAg/d=1/rs=AHpOoo8czmnaLIncRgBQP7N2THncpDJ9mQ/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20241104.0_p1","fr",null,0],[0.009999999776482582,"tn","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,1],[1,null,null,40400,425,"TUN","fr","699802849.0",8,null,1,0,null,null,null,null,"102118940",null,null,null,"yoJPZ77cCr7Np84PstOhoQU",0,0,0,null,2,5,"nn",12,0,0,0,0,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.Z8FBMQoacoc.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTt16WS-AyvNEln9-TaO-tZR_15utQ"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.zyyRgCCaN80.L.W.O/m=qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTs4SLbgh5FvGZPW_Ny7TyTdXfy6xA"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/1/widget/account?yac=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=fr\u0026continue=https://colab.research.google.com/%3Fauthuser%3D1\u0026ec=GBRAqQM",68,2,null,null,1,113,"Un problème est survenu.%1$s Actualisez pour réessayer ou %2$ssélectionnez un autre compte%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,1],0,0,1,["Alerte de sécurité critique","Alerte importante liée au compte","Alerte d'utilisation de l'espace de stockage",0,0],0,1,null,1,1,1,1,null,null,0,0,0,null,0,0],[null,null,[null,null,null,"https://ogs.google.com/u/1/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"fr",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=fr\u0026continue=https://colab.research.google.com/%3Fauthuser%3D1\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=fr\u0026continue=https://colab.research.google.com/%3Fauthuser%3D1\u0026timeStmp=1733264074\u0026secTok=.AG5fkS8QbWtXUUoW3azIILlC7zRoVKc2QA\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=1\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=fr\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026authuser=1\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F%3Fauthuser%3D1\u0026ec=GAZAqQM",1,1,0,0,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,1,"","",0,0,null,86400,null,0,1,null,0,null,0],0,null,null,null,0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ca,ja,ka,oa,qa,ra,Aa,Ba,Da,Ea,Fa,Ia,Ya,Xa,ab,cb,bb,db,eb,hb,ib,mb,pb,jb,ob,nb,lb,kb,qb,rb,yb,Cb,Db,Eb,Fb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.Jj=!0;return a};ca=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};
_.da=function(a){_.t.setTimeout(()=>{throw a;},0)};_.fa=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};ja=function(a){return ha?ia?ia.brands.some(({brand:b})=>b&&b.indexOf(a)!=-1):!1:!1};_.u=function(a){return _.fa().indexOf(a)!=-1};ka=function(){return ha?!!ia&&ia.brands.length>0:!1};_.la=function(){return ka()?!1:_.u("Opera")};_.ma=function(){return ka()?!1:_.u("Trident")||_.u("MSIE")};_.na=function(){return _.u("Firefox")||_.u("FxiOS")};
_.pa=function(){return _.u("Safari")&&!(oa()||(ka()?0:_.u("Coast"))||_.la()||(ka()?0:_.u("Edge"))||(ka()?ja("Microsoft Edge"):_.u("Edg/"))||(ka()?ja("Opera"):_.u("OPR"))||_.na()||_.u("Silk")||_.u("Android"))};oa=function(){return ka()?ja("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(ka()?0:_.u("Edge"))||_.u("Silk")};qa=function(){return ha?!!ia&&!!ia.platform:!1};ra=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.sa=function(){return ra()||_.u("iPad")||_.u("iPod")};
_.ta=function(){return qa()?ia.platform==="macOS":_.u("Macintosh")};_.va=function(a,b){return _.ua(a,b)>=0};_.wa=function(a){let b="",c=0;const d=a.length-10240;for(;c<d;)b+=String.fromCharCode.apply(null,a.subarray(c,c+=10240));b+=String.fromCharCode.apply(null,c?a.subarray(c):a);return btoa(b)};_.xa=function(a){return a!=null&&a instanceof Uint8Array};_.ya=function(a){return Array.prototype.slice.call(a)};_.za=function(a){return!!((a[_.v]|0)&2)};Aa=function(a,b){b[_.v]=(a|0)&-30975};
Ba=function(a,b){b[_.v]=(a|34)&-30941};Da=function(a){return!(!a||typeof a!=="object"||a.i!==Ca)};Ea=function(a){return a!==null&&typeof a==="object"&&!Array.isArray(a)&&a.constructor===Object};Fa=function(a){return!Array.isArray(a)||a.length?!1:(a[_.v]|0)&1?!0:!1};_.Ga=function(a){if(a&2)throw Error();};Ia=function(a,b){(b=_.Ha?b[_.Ha]:void 0)&&(a[_.Ha]=_.ya(b))};_.Ka=function(a,b){Ja=b;a=new a(b);Ja=void 0;return a};
_.La=function(a,b,c,d){var e;d=(e=d)!=null?e:0;a==null&&(a=Ja);Ja=void 0;if(a==null)e=96,c?(a=[c],e|=512):a=[],b&&(e=e&-33521665|(b&1023)<<15);else{if(!Array.isArray(a))throw Error("r");e=a[_.v]|0;if(e&2048)throw Error("u");if(e&64)return a;d===1||d===2||(e|=64);if(c&&(e|=512,c!==a[0]))throw Error("v");a:{d=a;c=e;if(e=d.length){const f=e-1;if(Ea(d[f])){c|=256;b=f-(+!!(c&512)-1);if(b>=1024)throw Error("w");e=c&-33521665|(b&1023)<<15;break a}}if(b){b=Math.max(b,e-(+!!(c&512)-1));if(b>1024)throw Error("x");
e=c&-33521665|(b&1023)<<15}else e=c}}a[_.v]=e;return a};_.Na=function(){const a=Error();Ma(a,"incident");_.da(a)};_.Oa=function(a){a=Error(a);Ma(a,"warning");return a};_.Qa=function(a){if(typeof a!=="boolean")throw Error("z`"+_.Pa(a)+"`"+a);return a};_.Ra=function(a){if(!Number.isFinite(a))throw _.Oa("enum");return a|0};_.Sa=function(a){if(typeof a!=="number")throw _.Oa("int32");if(!Number.isFinite(a))throw _.Oa("int32");return a|0};_.Ta=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Ua=function(a){return a==null||typeof a==="string"?a:void 0};_.Wa=function(a,b,c){if(a!=null&&typeof a==="object"&&a.Gd===_.Va)return a;if(Array.isArray(a)){var d=a[_.v]|0,e=d;e===0&&(e|=c&32);e|=c&2;e!==d&&(a[_.v]=e);return new b(a)}};Ya=function(a,b){return Xa(b)};
Xa=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "bigint":return(0,_.Za)(a)?Number(a):String(a);case "boolean":return a?1:0;case "object":if(a)if(Array.isArray(a)){if(Fa(a))return}else{if(_.xa(a))return _.wa(a);if("function"==typeof _.$a&&a instanceof _.$a)return a.j()}}return a};ab=function(a,b,c){const d=_.ya(a);var e=d.length;const f=b&256?d[e-1]:void 0;e+=f?-1:0;for(b=b&512?1:0;b<e;b++)d[b]=c(d[b]);if(f){b=d[b]={};for(const g in f)b[g]=c(f[g])}Ia(d,a);return d};
cb=function(a,b,c,d,e){if(a!=null){if(Array.isArray(a))a=Fa(a)?void 0:e&&(a[_.v]|0)&2?a:bb(a,b,c,d!==void 0,e);else if(Ea(a)){const f={};for(let g in a)f[g]=cb(a[g],b,c,d,e);a=f}else a=b(a,d);return a}};bb=function(a,b,c,d,e){const f=d||c?a[_.v]|0:0;d=d?!!(f&32):void 0;const g=_.ya(a);for(let h=0;h<g.length;h++)g[h]=cb(g[h],b,c,d,e);c&&(Ia(g,a),c(f,g));return g};db=function(a){return a.Gd===_.Va?a.toJSON():Xa(a)};
eb=function(a,b,c=Ba){if(a!=null){if(a instanceof Uint8Array)return b?a:new Uint8Array(a);if(Array.isArray(a)){var d=a[_.v]|0;if(d&2)return a;b&&(b=d===0||!!(d&32)&&!(d&64||!(d&16)));return b?(a[_.v]=(d|34)&-12293,a):bb(a,eb,d&4?Ba:c,!0,!0)}a.Gd===_.Va&&(c=a.ha,d=c[_.v],a=d&2?a:_.Ka(a.constructor,_.fb(c,d,!0)));return a}};_.fb=function(a,b,c){const d=c||b&2?Ba:Aa,e=!!(b&32);a=ab(a,b,f=>eb(f,e,d));a[_.v]=a[_.v]|32|(c?2:0);return a};
_.gb=function(a){const b=a.ha,c=b[_.v];return c&2?_.Ka(a.constructor,_.fb(b,c,!1)):a};hb=function(a){return a};ib=function(a){return a};mb=function(a,b,c,d){return jb(a,b,c,d,kb,lb)};pb=function(a,b,c,d){return jb(a,b,c,d,nb,ob)};
jb=function(a,b,c,d,e,f){if(!c.length&&!d)return 0;var g=0;let h=0,k=0;var l=0;let m=0;for(var p=c.length-1;p>=0;p--){var r=c[p];d&&p===c.length-1&&r===d||(l++,r!=null&&k++)}if(d)for(var q in d)p=+q,isNaN(p)||(m+=qb(p),h++,p>g&&(g=p));l=e(l,k)+f(h,g,m);q=k;p=h;r=g;let x=m;for(let D=c.length-1;D>=0;D--){var B=c[D];if(B==null||d&&D===c.length-1&&B===d)continue;B=D-b;const H=e(B,q)+f(p,r,x);H<l&&(a=1+B,l=H);p++;q--;x+=qb(B);r=Math.max(r,B)}b=e(0,0)+f(p,r,x);b<l&&(a=0,l=b);if(d){p=h;r=g;x=m;q=k;for(const D in d)d=
+D,isNaN(d)||d>=1024||(p--,q++,x-=D.length,g=e(d,q)+f(p,r,x),g<l&&(a=1+d,l=g))}return a};ob=function(a,b,c){return c+a*3+(a>1?a-1:0)};nb=function(a,b){return(a>1?a-1:0)+(a-b)*4};lb=function(a,b){return a==0?0:9*Math.max(1<<32-Math.clz32(a+a/2-1),4)<=b?a==0?0:a<4?100+(a-1)*16:a<6?148+(a-4)*16:a<12?244+(a-6)*16:a<22?436+(a-12)*19:a<44?820+(a-22)*17:52+32*a:40+4*b};kb=function(a){return 40+4*a};qb=function(a){return a>=100?a>=1E4?Math.ceil(Math.log10(1+a)):a<1E3?3:4:a<10?1:2};
rb=function(a,b,c,d){b=d+(+!!(b&512)-1);if(!(b<0||b>=a.length||b>=c))return a[b]};_.sb=function(a,b,c,d){const e=b>>15&1023||536870912;if(c>=e){let f,g=b;if(b&256)f=a[a.length-1];else{if(d==null)return g;f=a[e+(+!!(b&512)-1)]={};g|=256}f[c]=d;c<e&&(a[c+(+!!(b&512)-1)]=void 0);g!==b&&(a[_.v]=g);return g}a[c+(+!!(b&512)-1)]=d;b&256&&(a=a[a.length-1],c in a&&delete a[c]);return b};_.ub=function(a,b,c,d){a=a.ha;let e=a[_.v];d=_.tb(a,e,c,d);b=_.Wa(d,b,e);b!==d&&b!=null&&_.sb(a,e,c,b);return b};
_.vb=function(a,b){return a!=null?a:b};
yb=function(a){var b=wb?a.ha:bb(a.ha,db,void 0,void 0,!1);var c=!wb,d=(c?a.ha:b)[_.v];if(a=b.length){var e=b[a-1],f=Ea(e);f?a--:e=void 0;var g=+!!(d&512)-1,h=a-g;d=!!xb&&!(d&512);var k,l=(k=xb)!=null?k:ib;k=d?l(h,g,b,e):h;d=(h=d&&h!==k)?Array.prototype.slice.call(b,0,a):b;if(f||h){b:{var m=d;var p=e;var r;f=!1;if(h)for(l=Math.max(0,k+g);l<m.length;l++){var q=m[l];const D=l-g;if(!(q==null||Fa(q)||Da(q)&&q.size===0)){var x=m[l]=void 0;((x=r)!=null?x:r={})[D]=q;f=!0}}if(p)for(let D in p)if(x=+D,isNaN(x)){let H;
((H=r)!=null?H:r={})[D]=p[D]}else if(l=p[D],Array.isArray(l)&&(Fa(l)||Da(l)&&l.size===0)&&(l=null),l==null&&(f=!0),h&&x<k){f=!0;l=x+g;for(q=m.length;q<=l;q++)m.push(void 0);m[l]=p[x]}else if(l!=null){let H;((H=r)!=null?H:r={})[D]=l}f||(r=p);if(r)for(let D in r){p=r;break b}p=null}m=p==null?e!=null:p!==e}h&&(a=d.length);for(var B;a>0;a--){r=d[a-1];if(!(r==null||Fa(r)||Da(r)&&r.size===0))break;B=!0}if(d!==b||m||B){if(!h&&!c)d=Array.prototype.slice.call(d,0,a);else if(B||m||p)d.length=a;p&&d.push(p)}b=
d}return b};_.zb=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.w=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Ab=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Bb=function(a){for(const b in a)return!1;return!0};Cb=Object.defineProperty;
Db=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Eb=Db(this);Fb=function(a,b){if(b)a:{var c=Eb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Cb(c,a,{configurable:!0,writable:!0,value:b})}};
Fb("Symbol.dispose",function(a){return a?a:Symbol("b")});Fb("globalThis",function(a){return a||Eb});Fb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});var Ib,Jb,Mb;_.Gb=_.Gb||{};_.t=this||self;Ib=function(a,b){var c=_.Hb("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Jb=_.t._F_toggles||[];_.Hb=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Pa=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Kb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Lb="closure_uid_"+(Math.random()*1E9>>>0);
Mb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Mb;return _.z.apply(null,arguments)};_.Nb=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");var c=_.t;a[0]in c||typeof c.execScript=="undefined"||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};
_.C=function(a,b){function c(){}c.prototype=b.prototype;a.W=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Bj=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.C(_.aa,Error);_.aa.prototype.name="CustomError";var Ob=!!(Jb[0]&1024),Pb=!!(Jb[0]&32),Qb=!!(Jb[0]&2048),Rb=!!(Jb[0]&8);var Sb,ha;Sb=Ib(1,!0);ha=Ob?Qb:Ib(610401301,!1);_.Tb=Ob?Pb||!Rb:Ib(653718497,Sb);_.Ub=_.ba(a=>typeof a==="number");_.Vb=_.ba(a=>typeof a==="string");_.Wb=_.ba(a=>typeof a==="boolean");_.Xb=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var $b,Yb,ac,Zb;_.Za=_.ba(a=>_.Xb?a>=Yb&&a<=Zb:a[0]==="-"?ca(a,$b):ca(a,ac));$b=Number.MIN_SAFE_INTEGER.toString();Yb=_.Xb?BigInt(Number.MIN_SAFE_INTEGER):void 0;ac=Number.MAX_SAFE_INTEGER.toString();Zb=_.Xb?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.bc=typeof TextDecoder!=="undefined";_.cc=typeof TextEncoder!=="undefined";_.dc=function(){return _.fa().toLowerCase().indexOf("webkit")!=-1};var ia,ec=_.t.navigator;ia=ec?ec.userAgentData||null:null;_.ua=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.fc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.gc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.hc=function(a){_.hc[" "](a);return a};_.hc[" "]=function(){};var uc;_.ic=_.la();_.jc=_.ma();_.kc=_.u("Edge");_.lc=_.u("Gecko")&&!(_.dc()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.mc=_.dc()&&!_.u("Edge");_.nc=_.ta();_.oc=qa()?ia.platform==="Windows":_.u("Windows");_.pc=qa()?ia.platform==="Android":_.u("Android");_.qc=ra();_.rc=_.u("iPad");_.sc=_.u("iPod");_.tc=_.sa();
a:{let a="";const b=function(){const c=_.fa();if(_.lc)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.kc)return/Edge\/([\d\.]+)/.exec(c);if(_.jc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.mc)return/WebKit\/(\S+)/.exec(c);if(_.ic)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.jc){var vc;const c=_.t.document;vc=c?c.documentMode:void 0;if(vc!=null&&vc>parseFloat(a)){uc=String(vc);break a}}uc=a}_.wc=uc;_.xc=_.na();_.yc=ra()||_.u("iPod");_.zc=_.u("iPad");_.Ac=_.u("Android")&&!(oa()||_.na()||_.la()||_.u("Silk"));_.Bc=oa();_.Cc=_.pa()&&!_.sa();var Dc;_.v=Symbol();Dc=Symbol();_.Ec=Symbol();var Ca,Gc;_.Va={};Ca={};Gc=[];Gc[_.v]=55;_.Fc=Object.freeze(Gc);_.Hc=Object.freeze({});var Ja;var Ma=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};var Ic;_.Jc=function(a,b){a=a.ha;return _.tb(a,a[_.v],b)};_.tb=function(a,b,c,d){if(c===-1)return null;const e=b>>15&1023||536870912;if(c>=e){if(b&256)return a[a.length-1][c]}else{var f=a.length;if(d&&b&256&&(d=a[f-1][c],d!=null)){if(rb(a,b,e,c)&&Dc!=null){var g;a=(g=Ic)!=null?g:Ic={};g=a[Dc]||0;g>=4||(a[Dc]=g+1,_.Na())}return d}return rb(a,b,e,c)}};_.Kc=function(a,b,c){const d=a.ha;let e=d[_.v];_.Ga(e);_.sb(d,e,b,c);return a};
_.E=function(a,b,c,d=!1){b=_.ub(a,b,c,d);if(b==null)return b;a=a.ha;d=a[_.v];if(!(d&2)){const e=_.gb(b);e!==b&&(b=e,_.sb(a,d,c,b))}return b};_.F=function(a,b,c){c==null&&(c=void 0);return _.Kc(a,b,c)};_.G=function(a,b){a=_.Jc(a,b);return a==null||typeof a==="boolean"?a:typeof a==="number"?!!a:void 0};_.I=function(a,b){return _.Ua(_.Jc(a,b))};_.J=function(a,b,c=!1){return _.vb(_.G(a,b),c)};_.K=function(a,b){return _.vb(_.I(a,b),"")};_.M=function(a,b,c){return _.Kc(a,b,c==null?c:_.Qa(c))};
_.N=function(a,b,c){return _.Kc(a,b,c==null?c:_.Sa(c))};_.O=function(a,b,c){return _.Kc(a,b,_.Ta(c))};_.P=function(a,b,c){return _.Kc(a,b,c==null?c:_.Ra(c))};var xb,wb;_.Q=class{constructor(a,b,c){this.ha=_.La(a,b,c)}toJSON(){return yb(this)}Aa(a){try{return wb=!0,a&&(xb=a===ib||a!==hb&&a!==mb&&a!==pb?ib:a),JSON.stringify(yb(this),Ya)}finally{a&&(xb=void 0),wb=!1}}qc(){return _.za(this.ha)}};_.Q.prototype.Gd=_.Va;_.Q.prototype.toString=function(){try{return wb=!0,yb(this).toString()}finally{wb=!1}};_.Lc=_.zb();_.Mc=_.zb();_.Nc=_.zb();var Oc=class extends _.Q{constructor(){super()}};_.Pc=class extends _.Q{constructor(){super()}D(a){return _.N(this,3,a)}};var Qc=class extends _.Q{constructor(a){super(a)}Ic(a){return _.O(this,24,a)}};_.Rc=class extends _.Q{constructor(a){super(a)}};_.R=function(){this.qa=this.qa;this.Y=this.Y};_.R.prototype.qa=!1;_.R.prototype.isDisposed=function(){return this.qa};_.R.prototype.dispose=function(){this.qa||(this.qa=!0,this.O())};_.R.prototype[Symbol.dispose]=function(){this.dispose()};_.R.prototype.O=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Sc=class extends _.R{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}qb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].qb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Uc=class extends _.R{constructor(){var a=_.Tc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Vc=class extends _.Q{constructor(a){super(a)}};var Wc=class extends _.Q{constructor(a){super(a)}};var Zc;_.Xc=function(a,b,c=98,d=new _.Pc){if(a.i){const e=new Oc;_.O(e,1,b.message);_.O(e,2,b.stack);_.N(e,3,b.lineNumber);_.P(e,5,1);_.F(d,40,e);a.i.log(c,d)}};Zc=class{constructor(){var a=Yc;this.i=null;_.J(a,4,!0)}log(a,b,c=new _.Pc){_.Xc(this,a,98,c)}};var $c,ad;$c=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.fc(c,b,a)}catch(d){console.error(d)}}}};_.bd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new ad(a,b,c));$c(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.i=a;$c(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("D");this.j=a;$c(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
ad=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.cd=a=>{var b="nc";if(a.nc&&a.hasOwnProperty(b))return a.nc;b=new a;return a.nc=b};_.dd=class{constructor(){this.v=new _.bd;this.i=new _.bd;this.D=new _.bd;this.B=new _.bd;this.C=new _.bd;this.A=new _.bd;this.o=new _.bd;this.j=new _.bd;this.F=new _.bd}Y(){return this.v}M(){return this.i}N(){return this.D}L(){return this.B}qa(){return this.C}K(){return this.A}J(){return this.o}G(){return this.j}static i(){return _.cd(_.dd)}};var id;_.fd=function(){return _.E(_.ed,Qc,1)};_.gd=function(){return _.E(_.ed,_.Rc,5)};id=class extends _.Q{constructor(){super(hd)}};var hd;window.gbar_&&window.gbar_.CONFIG?hd=window.gbar_.CONFIG[0]||{}:hd=[];_.ed=new id;var Yc=_.E(_.ed,Wc,3)||new Wc;_.fd()||new Qc;_.Tc=new Zc;_.A("gbar_._DumpException",function(a){_.Tc?_.Tc.log(a):console.error(a)});_.jd=new Uc;var ld;_.md=function(a,b){var c=_.kd.i();if(a in c.i){if(c.i[a]!=b)throw new ld;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Bb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.kd=class{constructor(){this.i={};this.j={}}static i(){return _.cd(_.kd)}};_.nd=class extends _.aa{constructor(){super()}};ld=class extends _.nd{};_.A("gbar.A",_.bd);_.bd.prototype.aa=_.bd.prototype.then;_.A("gbar.B",_.dd);_.dd.prototype.ba=_.dd.prototype.M;_.dd.prototype.bb=_.dd.prototype.N;_.dd.prototype.bd=_.dd.prototype.qa;_.dd.prototype.bf=_.dd.prototype.Y;_.dd.prototype.bg=_.dd.prototype.L;_.dd.prototype.bh=_.dd.prototype.K;_.dd.prototype.bj=_.dd.prototype.J;_.dd.prototype.bk=_.dd.prototype.G;_.A("gbar.a",_.dd.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var od=new Sc;_.md("api",od);
var pd=_.gd()||new _.Rc,qd=window,rd=_.y(_.I(pd,8));qd.__PVT=rd;_.md("eq",_.jd);
}catch(e){_._DumpException(e)}
try{
_.sd=class extends _.Q{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var td=class extends _.Q{constructor(){super()}};var ud=class extends _.R{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.G(a,12)!=null&&(d.dpo=_.w(_.J(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.K(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.K(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var vd=_.E(_.ed,_.Vc,14);if(vd){var wd=_.E(_.ed,_.sd,9)||new _.sd,xd=new td,yd=new ud;yd.init(vd,wd,xd);_.md("gs",yd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_rimahben0@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./Analyse de données_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20241202-060120_RC00_701926325'; var colabScsVersion = '54a87adeda827cc4b5c1523f9f5252dd'; var hl = 'fr'; var colabExperiments = JSON.parse('\x7b\x22add_prompt_cell\x22: false, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 1000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_do_conversation_model_id\x22: \x22\x22, \x22aida_generate_code_model_id\x22: \x22\x22, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22cell_markdown_toolbar_tooltips\x22: true, \x22cell_output_actions_tooltip\x22: true, \x22cell_tags\x22: false, \x22cell_toolbar_ai_menu\x22: true, \x22cell_toolbar_tooltips\x22: true, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22chat_reduce_refusals\x22: true, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_text_compose\x22: true, \x22client_trim_completion_text\x22: 400, \x22cloud_origin\x22: \x22\x22, \x22code_report_millis\x22: 0, \x22commands_in_toolbar\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22compose_skip_suffix_check\x22: false, \x22converse_server_side_history\x22: false, \x22converse_temp\x22: \x22\x22, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22dbu\x22: \x22\x22, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22development\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_completions_backend_switching\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22execution_announcements\x22: true, \x22execution_status_propagation\x22: true, \x22explain_cell\x22: true, \x22explain_error\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22filter_repetitive_suggestions\x22: false, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22gemini_rebrand\x22: true, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_duplicate_code\x22: true, \x22generate_prompt_reduce_name_errors\x22: true, \x22generate_temp\x22: \x22\x22, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22granular_browser_permissions\x22: true, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22i18n_runtime_labels\x22: false, \x22import_data\x22: false, \x22import_gemini_api_key\x22: true, \x22interactive_sheet_next_steps\x22: true, \x22internal_chat\x22: false, \x22internal_schedule\x22: false, \x22is_prober\x22: false, \x22jsraw\x22: \x22compiled\x22, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22minimizable_comments\x22: false, \x22ml_enabled\x22: true, \x22mlpp\x22: false, \x22mlpp_multiline\x22: false, \x22mobile\x22: false, \x22move_converse_notebook_context_to_facts\x22: true, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22notebook_context_length\x22: 40000, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prereq_cells_next_steps\x22: true, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduce_chat_not_answering\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kws\x22: false, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: false, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt\x22: false, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_create_gemini_api_key_link\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_serving_config\x22: \x22pl_700m_smart_paste_3.0.25\x22, \x22smartpaste_tooltip\x22: false, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22task_service_max_poll_count\x22: 45, \x22task_service_poll_interval_ms\x22: 2000, \x22task_service_wait_before_polling_ms\x22: 5000, \x22term4all\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22tpu_v5e1\x22: false, \x22transform_code\x22: false, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22updated_inline_cell_diff\x22: false, \x22use_corplogin\x22: true, \x22use_dm_sql_lsp\x22: false, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22workstations\x22: false, \x22ids\x22: \x5b20730315, 20730177, 20730265, 20730333, 20730183, 20730262, 20730230, 20730253, 20730318, 20730324, 20730297, 20730330, 20730186, 20730345, 20730150\x5d, \x22flag_ids\x22: \x7b\x22add_prompt_cell\x22: 45644995, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_generate_code_model_id\x22: 45427663, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22cell_markdown_toolbar_tooltips\x22: 45654223, \x22cell_output_actions_tooltip\x22: 45650940, \x22cell_tags\x22: 45425779, \x22cell_toolbar_ai_menu\x22: 45647581, \x22cell_toolbar_tooltips\x22: 45649981, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22chat_reduce_refusals\x22: 45656767, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_text_compose\x22: 45425512, \x22client_trim_completion_text\x22: 45425628, \x22cloud_origin\x22: 45425538, \x22code_report_millis\x22: 45658073, \x22commands_in_toolbar\x22: 45425502, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22compose_skip_suffix_check\x22: 45615470, \x22converse_server_side_history\x22: 45634472, \x22converse_temp\x22: 45425509, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22dbu\x22: 45425545, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22development\x22: 45425544, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22enable_adhoc_backends\x22: 45425506, \x22enable_completions_backend_switching\x22: 45662651, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22execution_announcements\x22: 45651325, \x22execution_status_propagation\x22: 45644828, \x22explain_cell\x22: 45425505, \x22explain_error\x22: 45425487, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22filter_repetitive_suggestions\x22: 45615781, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22gemini_rebrand\x22: 45631310, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_duplicate_code\x22: 45646291, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22generate_temp\x22: 45425508, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22granular_browser_permissions\x22: 45630936, \x22hats_surveys\x22: 45425559, \x22i18n_runtime_labels\x22: 45662916, \x22import_data\x22: 45430411, \x22import_gemini_api_key\x22: 45654551, \x22interactive_sheet_next_steps\x22: 45634324, \x22internal_chat\x22: 45622872, \x22internal_schedule\x22: 45425578, \x22is_prober\x22: 45429104, \x22jsraw\x22: 45425557, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22minimizable_comments\x22: 45661083, \x22ml_enabled\x22: 45425493, \x22mlpp\x22: 45425608, \x22mlpp_multiline\x22: 45425623, \x22mobile\x22: 45425562, \x22move_converse_notebook_context_to_facts\x22: 45666389, \x22mpp_orc_temperature_override\x22: 45649914, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22notebook_context_length\x22: 45633457, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prereq_cells_next_steps\x22: 45640400, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduce_chat_not_answering\x22: 45640977, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kws\x22: 45650184, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt\x22: 45425624, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting\x22: 45647313, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_create_gemini_api_key_link\x22: 45644190, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_serving_config\x22: 45630585, \x22smartpaste_tooltip\x22: 45653721, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22tpu_v5e1\x22: 45652002, \x22transform_code\x22: 45667102, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22updated_inline_cell_diff\x22: 45667103, \x22use_corplogin\x22: 45425606, \x22use_dm_sql_lsp\x22: 45425610, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'rimahben0@gmail.com'; var colabRenderDataToken = 'AFWLbD1gzMOjS92Jup7egkZxIBogRjMvkv7LiTIEJ-AZXvZ6ucW3Lcvz5AELuIA2m0lIhmYZn_XBFbfb3o0KG3nYjjqIESSnhoIL'; var colabConfig = '\x5b\x5b\x22rimahben0@gmail.com\x22,\x5b1,\x22AHXL0D20ubE\/9r0wc0QhIVaCeXvPJ6Gb2x8AdZwzFT9S842GT8GmVX6xgzs1sz+xNs5AvypTUdmTJDwHuo0WlWwb4IrcYLj4HU5TXaT\/UERvGHIzgmidaWFgiXErOtd+dBtoneCqc6TebITBXXVLTh+bnAGK0OFXyClp7x2r6oCHU21JkuPti32ggwjLHaIXrMVUqqk2WGULmAR\/8hNvPvdX0hbmcBYhDnzGRqVQ2AecYXT6p+KUp41F6R\/v63XZKUdY7tm9TfRD\/iUxazBvQyueKgNMBOS\/EJuoR6De7udj0SwF+QGAiAPWiGI8qNv\/aNMSNzhod++jq3OIWSw2X0\/uyBhGe1Z3XqD3w75tCKb2DoC5Uoh7NasAqPM0n8tjnuVMMyqOvvQZr+PwfiZTxFV2nO72kwRLOA9wX1rX2eDRRJGu6D14ni\/jaiov4hgogmN+e0xBMy+Gnd8n\/lAgLDZxCocsT2gqJVcYeDbFm0jcnpkxxuw4tfAYSVQLiELy\/Y0uSKdofw8ynsLgO2fAVvQyPlzo3jwgkKDuonazmYHUjfuaheQH4oPH+fLkQBCoxFkCml7xrNK4gMtu3iHQsQIzgqtVuKfhPcSNKlrrK1pNLGz\/MQ\/nPD6LHkHLZPYoRtUJmxMI2ASYMRIrCVZzXP9XUo2S\/X2rVZFmi3rALiXi1Qi\/k0fQvefOsC73LgNmIbHMDcuN4c3S0WBffP5HZCJAinnYp+AvO7ER9MTvk4XbVLwYUiQ0VXaWeRKrVKXUIdoAQ+TWamMb50AKlhkgB2I8+FSG2iE1ot0eZkpNcDCUUtTVsLwfVjS3mBNauDXGdOEdmLX10v2Bmnn\/fy20R5+TkEcaLTfP2gDv6IpEUn\/jgauF6KZLcTDRbyiyRKjOjR4BcseLxa20+4fmwPJRggkHgDR\/OYe1u06LSVHkNdaxkTSfRDWLXac1okTspF3v\/N4bob7ZWxNhC8QeUY7n5zuDv1quh6Rgehumk1gbscw9TrDBuzt7RzZABuFkptZ4N7M68zeFmQL0gTbvNsPnrfrXRxG89USWdW3LltbWU8OrpMVzn0AlPUmNIlccq0MenlyfbDFuedz+n7c97JG2XcpwkaanSmjQMT5QSPIOSiDI7+JSKnm+WFJCB1O\/dcoa+yWqt7KOyaI0DzaQh\/XdWthPuquVoq9U58omd7uht762uyP3\/BlDZseXh67\/iEYi1+Iu09wsI8nvtFkJOnrrPyBugE\/wNcdrzKiKGlKMU0kcZ8GVgDSAtiPNmdTauAJHQZ50v6w0evPUVUYDLv31AL5l4ai+vfGTEmvooT091ay67YO5pbgq+Db7\/ZxfusKlpsVECamPkQpQ\/0eNTJFgY6Cl5aBxyzJRvZckA2pTN5hZjUiPuxYRU\/M8DbY\/zXLpzIUm8uKiFdBohPF7TJa6m52WDestzmHbzGE6\/1JhGKwjKjVszJzxfs2puyLsvBAKTD1PBNyM\/6qzF3coJMRKalJTQz9NA7TN0Bd6fxf1tT2mqLqIBNWXZSKqA+7Y7DoGRoWuW5D\/FRtT6kKM9LsmVhX4NAoiuudRZvZR8dYBZJSMsCf5zJLFtCABkrt3033qwOH4upwEgWm006M0OCr3bIc7OxQQc1XkUwrzyIO2saChpIla8No0dLAFF5\/doErAlxSwNBQAWKI5rq\/Fqp\/X3M\/SmH9laJ\/FJ4vrshdpmpPL6luqqgo8PECodPjTz81Y8wj6zfBS4KBM1Gb96WH0LWL7U8C\/9SntcWu51fXXfmpeVwM\/YJD1Vq+52rPw7F\/bAzsFr1y8H5Dt\/qmy4d3zkBkxi1DKy33vSQXqAlSChuDfLN8wsacVUNajYMdNCZjqkqAydiaBTe7cSauJd\/CHBTRamI1tf1iSCzgbcLyRy6O7ULADHyFhHvdraeiJaBG1Pk8DUi2Sbz9IqmdUv2rZNkW+oodKk+1OzNirb4f0uczcNVDMBe+wDhCnAdb6oICcLrP3cFpyLGj+4lXUF3UZN0W+RarFgQjVltxsJXULofFSwoRQ4T7Dy1pXKs0KL\/y+Vob6EhN7YnU1\x22,\x22AJ9oCCxUyWKGj3yr+Llzv2ainUaPnAbQGo1tyXp1msu2dRiy4jcZe+WOvRn3cSkvG6f\/ukehmbRuEx1z5oOwW7oJAEoZpWo4LHYY1Ag2hZFUW5ckf+SEggyqm85i3k9L4Y7Far0WoHBh\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22US$ 9,99\x22,\x22US$ 49,99\x22,\x22US$ 9,99\x22,\x22US$ 49,99\x22\x5d,\x5b1,4,5\x5d,\x22TN\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/54a87adeda827cc4b5c1523f9f5252dd/img%2Ffavicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="f5qdvL6RAXlBgHezvCLpPtvx2wU5ZgIzzPULroprlnA"><meta name="google-site-verification" content="-wL8iYJTC7X0zF9qBNDQUAd-P1ZkQUK-OhSgv4Wkf1M"><meta name="google-site-verification" content="o-EECwEDQeUpZv0jTmoGfCDX7dUI8Kul4ESepXmDnO0"><meta name="google-site-verification" content="sNOroO9gXrazN-oMODOm0Bs0_vw1R5QwZ-BfrSHn8Io"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="8P-D5fVWgUIhw8X2BxnKJbf5itK0zxX0QhoBjbJFTe8"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="v2MQvJk6wTiBarKTbe1mdivqYCVtw-5m6w0HDzV5X_4"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./Analyse de données_files/lazy.min.js.télécharger" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./Analyse de données_files/rs=AA2YrTt16WS-AyvNEln9-TaO-tZR_15utQ" nonce=""></script><link type="text/css" href="./Analyse de données_files/rs=AA2YrTs4SLbgh5FvGZPW_Ny7TyTdXfy6xA" rel="stylesheet"><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./Analyse de données_files/editor.main.js.télécharger"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./Analyse de données_files/editor.main.css"><script async="async" type="text/javascript" src="./Analyse de données_files/editor.main.nls.js.télécharger"></script><script src="./Analyse de données_files/api.js.télécharger" nonce=""></script><script src="./Analyse de données_files/api(1).js.télécharger" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #f7f7f7; }
.monaco-editor .view-overlays .current-line { border: 2px solid #eeeeee; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #eeeeee; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(4, 49, 250, 0.3); --guide-color-active: #0431fa; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(49, 147, 49, 0.3); --guide-color-active: #319331; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(123, 56, 20, 0.3); --guide-color-active: #7b3814; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(153, 153, 153, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #000000; border-color: #000000; color: #ffffff; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #0431fa; }
.monaco-editor .bracket-highlighting-1 { color: #319331; }
.monaco-editor .bracket-highlighting-2 { color: #7b3814; }
.monaco-editor .bracket-highlighting-3 { color: #0431fa; }
.monaco-editor .bracket-highlighting-4 { color: #319331; }
.monaco-editor .bracket-highlighting-5 { color: #7b3814; }
.monaco-editor .bracket-highlighting-6 { color: #0431fa; }
.monaco-editor .bracket-highlighting-7 { color: #319331; }
.monaco-editor .bracket-highlighting-8 { color: #7b3814; }
.monaco-editor .bracket-highlighting-9 { color: #0431fa; }
.monaco-editor .bracket-highlighting-10 { color: #319331; }
.monaco-editor .bracket-highlighting-11 { color: #7b3814; }
.monaco-editor .bracket-highlighting-12 { color: #0431fa; }
.monaco-editor .bracket-highlighting-13 { color: #319331; }
.monaco-editor .bracket-highlighting-14 { color: #7b3814; }
.monaco-editor .bracket-highlighting-15 { color: #0431fa; }
.monaco-editor .bracket-highlighting-16 { color: #319331; }
.monaco-editor .bracket-highlighting-17 { color: #7b3814; }
.monaco-editor .bracket-highlighting-18 { color: #0431fa; }
.monaco-editor .bracket-highlighting-19 { color: #319331; }
.monaco-editor .bracket-highlighting-20 { color: #7b3814; }
.monaco-editor .bracket-highlighting-21 { color: #0431fa; }
.monaco-editor .bracket-highlighting-22 { color: #319331; }
.monaco-editor .bracket-highlighting-23 { color: #7b3814; }
.monaco-editor .bracket-highlighting-24 { color: #0431fa; }
.monaco-editor .bracket-highlighting-25 { color: #319331; }
.monaco-editor .bracket-highlighting-26 { color: #7b3814; }
.monaco-editor .bracket-highlighting-27 { color: #0431fa; }
.monaco-editor .bracket-highlighting-28 { color: #319331; }
.monaco-editor .bracket-highlighting-29 { color: #7b3814; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23e51400'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23bf8803'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%231a85ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22%236c6c6c%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.467; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.15); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(34, 34, 34, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(34, 34, 34, 0.2) 50%, rgba(34, 34, 34, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #a8ac94; }
.monaco-editor .findScope { background-color: rgba(180, 180, 180, 0.3); }
.monaco-editor .find-widget { background-color: #f3f3f3; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.16); }
.monaco-editor .find-widget { color: #616161; }
.monaco-editor .find-widget.no-results .matchesCount { color: #a1260d; }
.monaco-editor .find-widget .monaco-sash { background-color: #c8c8c8; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(184, 184, 184, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #0090f1; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(200, 200, 200, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(200, 200, 200, 0.5); }
.monaco-editor { --vscode-foreground: #616161;
--vscode-disabledForeground: rgba(97, 97, 97, 0.5);
--vscode-errorForeground: #a1260d;
--vscode-descriptionForeground: #717171;
--vscode-icon-foreground: #424242;
--vscode-focusBorder: #0090f1;
--vscode-textSeparator-foreground: rgba(0, 0, 0, 0.18);
--vscode-textLink-foreground: #006ab1;
--vscode-textLink-activeForeground: #006ab1;
--vscode-textPreformat-foreground: #a31515;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(220, 220, 220, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.16);
--vscode-input-background: #ffffff;
--vscode-input-foreground: #616161;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-inputOption-activeBackground: rgba(0, 144, 241, 0.2);
--vscode-inputOption-activeForeground: #000000;
--vscode-input-placeholderForeground: rgba(97, 97, 97, 0.5);
--vscode-inputValidation-infoBackground: #d6ecf2;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #f6f5d2;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #f2dede;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #ffffff;
--vscode-dropdown-foreground: #616161;
--vscode-dropdown-border: #cecece;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #007acc;
--vscode-button-hoverBackground: #0062a3;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #5f6a79;
--vscode-button-secondaryHoverBackground: #4c5561;
--vscode-badge-background: #c4c4c4;
--vscode-badge-foreground: #333333;
--vscode-scrollbar-shadow: #dddddd;
--vscode-scrollbarSlider-background: rgba(100, 100, 100, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(0, 0, 0, 0.6);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #e51400;
--vscode-editorWarning-foreground: #bf8803;
--vscode-editorInfo-foreground: #1a85ff;
--vscode-editorHint-foreground: #6c6c6c;
--vscode-sash-hoverBorder: #0090f1;
--vscode-editor-background: #f7f7f7;
--vscode-editor-foreground: #000000;
--vscode-editorStickyScroll-background: #f7f7f7;
--vscode-editorStickyScrollHover-background: #f0f0f0;
--vscode-editorWidget-background: #f3f3f3;
--vscode-editorWidget-foreground: #616161;
--vscode-editorWidget-border: #c8c8c8;
--vscode-quickInput-background: #f3f3f3;
--vscode-quickInput-foreground: #616161;
--vscode-quickInputTitle-background: rgba(0, 0, 0, 0.06);
--vscode-pickerGroup-foreground: #0066bf;
--vscode-pickerGroup-border: #cccedb;
--vscode-keybindingLabel-background: rgba(221, 221, 221, 0.4);
--vscode-keybindingLabel-foreground: #555555;
--vscode-keybindingLabel-border: rgba(204, 204, 204, 0.4);
--vscode-keybindingLabel-bottomBorder: rgba(187, 187, 187, 0.4);
--vscode-editor-selectionBackground: #add6ff;
--vscode-editor-inactiveSelectionBackground: #e5ebf1;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.3);
--vscode-editor-findMatchBackground: #a8ac94;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(180, 180, 180, 0.3);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: #616161;
--vscode-editor-hoverHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editorHoverWidget-background: #f3f3f3;
--vscode-editorHoverWidget-foreground: #616161;
--vscode-editorHoverWidget-border: #c8c8c8;
--vscode-editorHoverWidget-statusBarBackground: #e7e7e7;
--vscode-editorLink-activeForeground: #0000ff;
--vscode-editorInlayHint-foreground: #616161;
--vscode-editorInlayHint-background: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-typeForeground: #616161;
--vscode-editorInlayHint-typeBackground: rgba(196, 196, 196, 0.3);
--vscode-editorInlayHint-parameterForeground: #616161;
--vscode-editorInlayHint-parameterBackground: rgba(196, 196, 196, 0.3);
--vscode-editorLightBulb-foreground: #ddb100;
--vscode-editorLightBulbAutoFix-foreground: #007acc;
--vscode-diffEditor-insertedTextBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedTextBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-insertedLineBackground: rgba(155, 185, 85, 0.09);
--vscode-diffEditor-removedLineBackground: rgba(255, 0, 0, 0.03);
--vscode-diffEditor-diagonalFill: rgba(34, 34, 34, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #e4e4e4;
--vscode-diffEditor-unchangedRegionForeground: #4d4c4c;
--vscode-diffEditor-unchangedCodeBackground: rgba(184, 184, 184, 0.16);
--vscode-list-focusOutline: #0090f1;
--vscode-list-activeSelectionBackground: #d6ebff;
--vscode-list-activeSelectionForeground: #000000;
--vscode-list-inactiveSelectionBackground: #e4e6f1;
--vscode-list-hoverBackground: #f0f0f0;
--vscode-list-dropBackground: #d6ebff;
--vscode-list-highlightForeground: #0066bf;
--vscode-list-focusHighlightForeground: #0066bf;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #b01011;
--vscode-list-warningForeground: #855f00;
--vscode-listFilterWidget-background: #f3f3f3;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.16);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #a9a9a9;
--vscode-tree-inactiveIndentGuidesStroke: rgba(169, 169, 169, 0.4);
--vscode-tree-tableColumnsBorder: rgba(97, 97, 97, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(97, 97, 97, 0.04);
--vscode-list-deemphasizedForeground: #8e8e90;
--vscode-checkbox-background: #ffffff;
--vscode-checkbox-selectBackground: #f3f3f3;
--vscode-checkbox-foreground: #616161;
--vscode-checkbox-border: #cecece;
--vscode-checkbox-selectBorder: #424242;
--vscode-quickInputList-focusForeground: #000000;
--vscode-quickInputList-focusBackground: #d6ebff;
--vscode-menu-foreground: #616161;
--vscode-menu-background: #ffffff;
--vscode-menu-selectionForeground: #000000;
--vscode-menu-selectionBackground: #d6ebff;
--vscode-menu-separatorBackground: #d4d4d4;
--vscode-toolbar-hoverBackground: rgba(184, 184, 184, 0.31);
--vscode-toolbar-activeBackground: rgba(166, 166, 166, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(10, 50, 100, 0.2);
--vscode-editor-snippetFinalTabstopHighlightBorder: rgba(10, 50, 100, 0.5);
--vscode-breadcrumb-foreground: rgba(97, 97, 97, 0.8);
--vscode-breadcrumb-background: #f7f7f7;
--vscode-breadcrumb-focusForeground: #4e4e4e;
--vscode-breadcrumb-activeSelectionForeground: #4e4e4e;
--vscode-breadcrumbPicker-background: #f3f3f3;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(0, 0, 0, 0);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #c9c9c9;
--vscode-minimap-selectionHighlight: #add6ff;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #bf8803;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(100, 100, 100, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(0, 0, 0, 0.3);
--vscode-problemsErrorIcon-foreground: #e51400;
--vscode-problemsWarningIcon-foreground: #bf8803;
--vscode-problemsInfoIcon-foreground: #1a85ff;
--vscode-charts-foreground: #616161;
--vscode-charts-lines: rgba(97, 97, 97, 0.5);
--vscode-charts-red: #e51400;
--vscode-charts-blue: #1a85ff;
--vscode-charts-yellow: #bf8803;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #388a34;
--vscode-charts-purple: #652d90;
--vscode-symbolIcon-arrayForeground: #616161;
--vscode-symbolIcon-booleanForeground: #616161;
--vscode-symbolIcon-classForeground: #d67e00;
--vscode-symbolIcon-colorForeground: #616161;
--vscode-symbolIcon-constantForeground: #616161;
--vscode-symbolIcon-constructorForeground: #652d90;
--vscode-symbolIcon-enumeratorForeground: #d67e00;
--vscode-symbolIcon-enumeratorMemberForeground: #007acc;
--vscode-symbolIcon-eventForeground: #d67e00;
--vscode-symbolIcon-fieldForeground: #007acc;
--vscode-symbolIcon-fileForeground: #616161;
--vscode-symbolIcon-folderForeground: #616161;
--vscode-symbolIcon-functionForeground: #652d90;
--vscode-symbolIcon-interfaceForeground: #007acc;
--vscode-symbolIcon-keyForeground: #616161;
--vscode-symbolIcon-keywordForeground: #616161;
--vscode-symbolIcon-methodForeground: #652d90;
--vscode-symbolIcon-moduleForeground: #616161;
--vscode-symbolIcon-namespaceForeground: #616161;
--vscode-symbolIcon-nullForeground: #616161;
--vscode-symbolIcon-numberForeground: #616161;
--vscode-symbolIcon-objectForeground: #616161;
--vscode-symbolIcon-operatorForeground: #616161;
--vscode-symbolIcon-packageForeground: #616161;
--vscode-symbolIcon-propertyForeground: #616161;
--vscode-symbolIcon-referenceForeground: #616161;
--vscode-symbolIcon-snippetForeground: #616161;
--vscode-symbolIcon-stringForeground: #616161;
--vscode-symbolIcon-structForeground: #616161;
--vscode-symbolIcon-textForeground: #616161;
--vscode-symbolIcon-typeParameterForeground: #616161;
--vscode-symbolIcon-unitForeground: #616161;
--vscode-symbolIcon-variableForeground: #007acc;
--vscode-editor-lineHighlightBorder: #eeeeee;
--vscode-editor-rangeHighlightBackground: rgba(253, 255, 0, 0.2);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #000000;
--vscode-editorWhitespace-foreground: rgba(51, 51, 51, 0.2);
--vscode-editorIndentGuide-background: #d3d3d3;
--vscode-editorIndentGuide-activeBackground: #939393;
--vscode-editorLineNumber-foreground: #999999;
--vscode-editorActiveLineNumber-foreground: #0b216f;
--vscode-editorLineNumber-activeForeground: #0b216f;
--vscode-editorRuler-foreground: #d3d3d3;
--vscode-editorCodeLens-foreground: #919191;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #b9b9b9;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #f7f7f7;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.47);
--vscode-editorGhostText-foreground: rgba(0, 0, 0, 0.47);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #bf8803;
--vscode-editorOverviewRuler-infoForeground: #1a85ff;
--vscode-editorBracketHighlight-foreground1: #0431fa;
--vscode-editorBracketHighlight-foreground2: #319331;
--vscode-editorBracketHighlight-foreground3: #7b3814;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #cea33d;
--vscode-editorUnicodeHighlight-background: rgba(206, 163, 61, 0.08);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.25);
--vscode-editor-wordHighlightStrongBackground: #d6ebff;
--vscode-editor-wordHighlightTextBackground: rgba(173, 214, 255, 0.45);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(0, 0, 0, 0);
--vscode-peekViewTitle-background: #f3f3f3;
--vscode-peekViewTitleLabel-foreground: #000000;
--vscode-peekViewTitleDescription-foreground: #616161;
--vscode-peekView-border: #1a85ff;
--vscode-peekViewResult-background: #f3f3f3;
--vscode-peekViewResult-lineForeground: #646465;
--vscode-peekViewResult-fileForeground: #1e1e1e;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #6c6c6c;
--vscode-peekViewEditor-background: #f2f8fc;
--vscode-peekViewEditorGutter-background: #f2f8fc;
--vscode-peekViewEditorStickyScroll-background: #f2f8fc;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(245, 216, 2, 0.87);
--vscode-editorMarkerNavigationError-background: #e51400;
--vscode-editorMarkerNavigationError-headerBackground: rgba(229, 20, 0, 0.1);
--vscode-editorMarkerNavigationWarning-background: #bf8803;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(191, 136, 3, 0.1);
--vscode-editorMarkerNavigationInfo-background: #1a85ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(26, 133, 255, 0.1);
--vscode-editorMarkerNavigation-background: #f7f7f7;
--vscode-editorHoverWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-background: #f3f3f3;
--vscode-editorSuggestWidget-border: #c8c8c8;
--vscode-editorSuggestWidget-foreground: #000000;
--vscode-editorSuggestWidget-selectedForeground: #000000;
--vscode-editorSuggestWidget-selectedBackground: #d6ebff;
--vscode-editorSuggestWidget-highlightForeground: #0066bf;
--vscode-editorSuggestWidget-focusHighlightForeground: #0066bf;
--vscode-editorSuggestWidgetStatus-foreground: rgba(0, 0, 0, 0.5);
--vscode-editor-foldBackground: rgba(173, 214, 255, 0.3);
--vscode-editorGutter-foldingControlForeground: #424242; }

.mtk1 { color: #000000; }
.mtk2 { color: #f7f7f7; }
.mtk3 { color: #808080; }
.mtk4 { color: #ff0000; }
.mtk5 { color: #0451a5; }
.mtk6 { color: #0000ff; }
.mtk7 { color: #098658; }
.mtk8 { color: #008000; }
.mtk9 { color: #dd0000; }
.mtk10 { color: #811f3f; }
.mtk11 { color: #e00000; }
.mtk12 { color: #116644; }
.mtk13 { color: #383838; }
.mtk14 { color: #257693; }
.mtk15 { color: #795e26; }
.mtk16 { color: #001080; }
.mtk17 { color: #cd3131; }
.mtk18 { color: #863b00; }
.mtk19 { color: #af00db; }
.mtk20 { color: #c43b3b; }
.mtk21 { color: #800000; }
.mtk22 { color: #3030c0; }
.mtk23 { color: #666666; }
.mtk24 { color: #778899; }
.mtk25 { color: #c700c7; }
.mtk26 { color: #a31515; }
.mtk27 { color: #4f76ac; }
.mtk28 { color: #008080; }
.mtk29 { color: #001188; }
.mtk30 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style><script async="async" type="text/javascript" src="./Analyse de données_files/markdown.js.télécharger"></script><script async="async" type="text/javascript" src="./Analyse de données_files/python.js.télécharger"></script></head><body class="" style="overscroll-behavior: contain;"><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource.html"></iframe><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource(1).html"></iframe><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource(2).html"></iframe><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource(3).html"></iframe><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource(4).html"></iframe><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource(5).html"></iframe><iframe tabindex="-1" aria-hidden="true" style="position: absolute; width: 9em; height: 9em; top: -99em;" src="./Analyse de données_files/saved_resource(6).html"></iframe><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./Analyse de données_files/gapi_loader.js.télécharger" nonce=""></script><script src="./Analyse de données_files/socketio_binary.js.télécharger" nonce=""></script><script src="./Analyse de données_files/analytics_binary.js.télécharger" nonce=""></script><script src="./Analyse de données_files/MathJax.js.télécharger" nonce=""></script><script src="./Analyse de données_files/js_monaco_editor_vs_loader.js.télécharger" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./Analyse de données_files/external_binary_l10n__fr.js.télécharger" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$846942102$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$846942102$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Mise à jour de l'aperçu…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Fermer" data-aria-label="Fermer" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fermer">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar__surface {
          background-color: var(--colab-snackbar-surface-color);
        }
      </style>
      <!--?lit$846942102$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$846942102$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Chargement…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Fermer" data-aria-label="Fermer" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fermer">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_R" ng-non-bindable=""><div class="gb_Ac"><div>Compte Google</div><div class="gb_g">Rimah Ben0</div><div>rimahben0@gmail.com</div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Dd;Dd=class extends _.nd{};_.Ed=function(a,b){if(b in a.i)return a.i[b];throw new Dd;};_.Fd=function(a){return _.Ed(_.kd.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Id;_.Gd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Id=function(a){return new _.Hd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Jd=globalThis.trustedTypes;_.Kd=class{constructor(a){this.i=a}toString(){return this.i}};_.Ld=new _.Kd("about:invalid#zClosurez");_.Hd=class{constructor(a){this.ih=a}};_.Md=[Id("data"),Id("http"),Id("https"),Id("mailto"),Id("ftp"),new _.Hd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Nd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Od=new _.Nd(_.Jd?_.Jd.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Sd,fe,Rd,Td,Yd;_.Pd=function(a){return a==null?a:Number.isFinite(a)?a|0:void 0};_.Qd=function(a){if(a==null)return a;if(typeof a==="string"){if(!a)return;a=+a}if(typeof a==="number")return Number.isFinite(a)?a|0:void 0};Sd=function(){let a=null;if(!Rd)return a;try{const b=c=>c;a=Rd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Ud=function(){Td===void 0&&(Td=Sd());return Td};
_.Wd=function(a){const b=_.Ud();return new _.Vd(b?b.createScriptURL(a):a)};_.Xd=function(a){if(a instanceof _.Vd)return a.i;throw Error("F");};_.Zd=function(a){if(Yd.test(a))return a};_.$d=function(a){if(a instanceof _.Kd)if(a instanceof _.Kd)a=a.i;else throw Error("F");else a=_.Zd(a);return a};_.ae=function(a,b=document){let c,d;b=(d=(c="document"in b?b.document:b).querySelector)==null?void 0:d.call(c,`${a}[nonce]`);return b==null?"":b.nonce||b.getAttribute("nonce")||""};
_.be=function(a){var b=_.Pa(a);return b=="array"||b=="object"&&typeof a.length=="number"};_.ce=function(a,b,c){return _.ub(a,b,c,!1)!==void 0};_.de=function(a,b){return _.Qd(_.Jc(a,b))};_.S=function(a,b){return _.Pd(_.Jc(a,b))};_.T=function(a,b,c=0){return _.vb(_.de(a,b),c)};_.ee=function(a,b,c=0){return _.vb(_.S(a,b),c)};_.ge=function(a,b){return a.lastIndexOf(b,0)==0};Rd=_.Jd;_.Vd=class{constructor(a){this.i=a}toString(){return this.i+""}};Yd=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var le,pe,he;_.je=function(a){return a?new he(_.ie(a)):fe||(fe=new he)};_.ke=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.U=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a?a=(b||c).querySelector(a?"."+a:""):(b=b||c,a=(a?b.querySelectorAll(a?"."+a:""):b.getElementsByTagName("*"))[0]||null));return a||null};
_.me=function(a,b){_.Ab(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:le.hasOwnProperty(d)?a.setAttribute(le[d],c):_.ge(d,"aria-")||_.ge(d,"data-")?a.setAttribute(d,c):a[d]=c})};le={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.ne=function(a){return a?a.defaultView:window};_.qe=function(a,b){const c=b[1],d=_.oe(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.me(d,c));b.length>2&&pe(a,d,b);return d};pe=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.be(f)||_.Kb(f)&&f.nodeType>0?d(f):_.fc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Gd(f):f,d)}};
_.re=function(a){return _.oe(document,a)};_.oe=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.se=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.te=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.ue=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ie=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};he=function(a){this.i=a||_.t.document||document};_.n=he.prototype;
_.n.H=function(a){return _.ke(this.i,a)};_.n.Xa=function(a,b,c){return _.qe(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.xe=_.se;_.n.Uf=_.te;_.n.Tf=_.ue;
}catch(e){_._DumpException(e)}
try{
_.Gi=function(a){const b=_.ae("script",a.ownerDocument&&a.ownerDocument.defaultView||window);b&&a.setAttribute("nonce",b)};_.Hi=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.Wd(a);return b};_.Ii=class extends _.Q{constructor(a){super(a)}};_.Ji=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Li=function(a,b,c){a<b?Ki(a+1,b):_.Tc.log(Error("da`"+a+"`"+b),{url:c})},Ki=function(a,b){if(Mi){const c=_.re("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.Xd(Mi);_.Gi(c);c.onerror=_.Nb(Li,a,b,c.src);_.Ji("HEAD")[0].appendChild(c)}},Ni=class extends _.Q{constructor(a){super(a)}};var Oi=_.E(_.ed,Ni,17)||new Ni,Pi,Mi=(Pi=_.E(Oi,_.Ii,1))?_.Hi(Pi):null,Qi,Ri=(Qi=_.E(Oi,_.Ii,2))?_.Hi(Qi):null,Si=function(){Ki(1,2);if(Ri){const a=_.re("LINK");a.setAttribute("type","text/css");a.href=_.Xd(Ri).toString();a.rel="stylesheet";let b=_.ae("style",window);b&&a.setAttribute("nonce",b);_.Ji("HEAD")[0].appendChild(a)}};(function(){const a=_.fd();if(_.G(a,18))Si();else{const b=_.de(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Si,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./Analyse de données_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <div class="top-floater"><div role="banner">
    <colab-header-skip-button><template shadowrootmode="open"><!----><a id="skiplink" class="skip-link" href="https://colab.research.google.com/drive/1ePorOpCgRwO3hvAjOLVd-PUSZpysM-wW?authuser=1#top-toolbar"><!--?lit$846942102$-->Passer au contenu principal</a></template></colab-header-skip-button>
    <!--?lit$846942102$-->
    <!--?lit$846942102$-->
    <!--?lit$846942102$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning hidden">
            <!--?lit$846942102$-->Ce notebook a été ouvert avec des éléments de sortie privés. Ces éléments ne seront pas enregistrés. Vous pouvez désactiver cette option dans <a href="https://colab.research.google.com/drive/1ePorOpCgRwO3hvAjOLVd-PUSZpysM-wW?authuser=1#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Paramètres du notebook</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ouvrir les paramètres du notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
          <mwc-icon-button class="close" icon="close" title="Fermer"><template shadowrootmode="open"><!----><button class="mdc-icon-button mdc-icon-button--display-flex" aria-label="Fermer"><!--?lit$846942102$-->
    <!--?lit$846942102$--><i class="material-icons"><!--?lit$846942102$-->close</i>
    <span><slot></slot></span>
  </button></template></mwc-icon-button></div>
        

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><div id="header-logo">
              <!--?lit$846942102$--> <!--?lit$846942102$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=1" aria-label="Afficher dans Google Drive">
        <!--?lit$846942102$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$846942102$--> <!--?lit$846942102$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stocké dans Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Nom du notebook" command="rename" aria-describedby="doc-name-tooltip" style="width: 229.258px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events></input><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Renommer le notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Analyse_de_données.ipynb_</colab-input-sizer>
            <!--?lit$846942102$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Ajouter aux favoris" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Ajouter aux favoris">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ajouter le notebook aux favoris dans Google&nbsp;Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$846942102$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Fichier</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Modifier</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Affichage</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Insérer</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Exécution</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Outils</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$846942102$-->Aide</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div>
    <div id="colab-menu-cover" style="left: 391.99px; top: 60.9826px; width: 48px; display: none;"> </div></div><!----><colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$846942102$-->Toutes les modifications ont été enregistrées</button></template></colab-last-saved-indicator></div></div>
        <div id="header-right">
          <!--?lit$846942102$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$846942102$-->
      <!--?lit$846942102$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$846942102$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Ouvrir le volet des commentaires" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Ouvrir le volet des commentaires">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ouvrir le volet des commentaires</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$846942102$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Ouvrir les paramètres" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Ouvrir les paramètres">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ouvrir les paramètres</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$846942102$--> <md-text-button id="share-toolbar-button" command="share" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->people</md-icon>
                <!--?lit$846942102$-->Partager
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Partager le notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Ea gb_Id gb_2d gb_Vc" id="gb"><div class="gb_Bd gb_Zd gb_wd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Re" style="display:block"><div class="gb_2c"></div><div class="gb_y gb_bd gb_Nf gb_Z"><div class="gb_C gb_ib gb_Nf gb_Z"><a class="gb_A gb_Xa gb_Z" aria-expanded="false" aria-label="Compte Google Rimah Ben0  
(rimahben0@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=fr&amp;continue=https://colab.research.google.com/%3Fauthuser%3D1&amp;ec=GBRAqQM" tabindex="0" role="button"><img class="gb_O gbii" src="./Analyse de données_files/unnamed.png" srcset="https://lh3.google.com/u/1/ogw/AF2bZygI6TDgZR3x2Q-OViRK7ARirIYVkUMH27t59fj2ZyTjyw=s32-c-mo 1x, https://lh3.google.com/u/1/ogw/AF2bZygI6TDgZR3x2Q-OViRK7ARirIYVkUMH27t59fj2ZyTjyw=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;" aria-hidden="true"><iframe role="presentation" frameborder="0" scrolling="no" name="account" src="./Analyse de données_files/saved_resource(7).html" style="height: 100%; width: 100%; color-scheme: light; visibility: hidden;"></iframe></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.zd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.zd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("B`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Ad=document.querySelector(".gb_I .gb_A"),Bd=document.querySelector("#gb.gb_Rc");Ad&&!Bd&&_.zd(_.jd,Ad,"click");
}catch(e){_._DumpException(e)}
try{
_.gh=function(a){const b=[];let c=0;for(const d in a)b[c++]=a[d];return b};_.hh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ma()&&a.i[b].B())return a.i[b];return null};_.ih=function(a,b){a.i[b.K()]=b};var jh=new class extends _.R{constructor(){var a=_.Tc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.hh(this)&&_.hh(this).K()==a||this.i[a].R(!0))}Sa(a){this.j=a;for(const b in this.i)this.i[b].ma()&&this.i[b].Sa(a)}jc(a){return a in this.i?this.i[a]:null}};_.md("dd",jh);
}catch(e){_._DumpException(e)}
try{
_.Ai=function(a,b){return _.M(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Bi=document.querySelector(".gb_y .gb_A"),Ci=document.querySelector("#gb.gb_Rc");Bi&&!Ci&&_.zd(_.jd,Bi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><div class="notebook-horizontal">
        <!--?lit$846942102$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Sommaire" title="Sommaire" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Sommaire" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button toggle="" command="find" data-aria-label="Rechercher et remplacer" title="Rechercher et remplacer" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Rechercher et remplacer" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->search</md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button toggle="" command="show-variables" data-aria-label="Variables" title="Variables" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Variables" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$-->
      <path d="M4.51,9.44V6.08c0-1.34.37-1.85,1.6-2.17l.22-.06V3.13l-.27,0-.44,0a4.46,4.46,0,0,0-2.2.59,2.78,2.78,0,0,0-1,2.51V9.74c0,1.26-.26,1.61-1.49,2L0,12l.94.29c1.21.38,1.49.75,1.49,2v3.5a2.94,2.94,0,0,0,1,2.6,4.39,4.39,0,0,0,2.14.56l.46,0,.27,0v-.72l-.22-.06c-1.24-.32-1.6-.81-1.6-2.17V14.58c0-1.43-.3-2.13-1.25-2.57C4.2,11.57,4.51,10.87,4.51,9.44Z"></path>
      <path d="M23.06,11.71c-1.22-.36-1.49-.71-1.49-2l0-3.5a3,3,0,0,0-1-2.6,4.38,4.38,0,0,0-2.14-.56l-.46,0-.27,0v.72l.22.06c1.24.32,1.6.81,1.6,2.17V9.44c0,1.44.3,2.13,1.25,2.57-1,.44-1.25,1.14-1.25,2.57v3.36c0,1.34-.37,1.85-1.6,2.17l-.22.06v.72l.27,0,.44,0a4.47,4.47,0,0,0,2.2-.59,2.82,2.82,0,0,0,1-2.51V14.28c0-1.26.26-1.61,1.49-2L24,12Z"></path>
      <path d="M15.16,8.22a.88.88,0,0,1,.46.16,1.25,1.25,0,0,0,.69.2h0A1,1,0,0,0,17,8.23a1.06,1.06,0,0,0,.24-.8,1.1,1.1,0,0,0-1.15-1h0c-1,0-1.73.64-3,2.57l-.12-.51c-.28-1.36-.56-2-1.39-2h0A8,8,0,0,0,9,7.08l-.47.16.16.91L9.41,8a3.22,3.22,0,0,1,.73-.14c.34,0,.43,0,.71,1.2l.56,2.47L9.76,13.82a3.6,3.6,0,0,1-.8.88.9.9,0,0,1-.38-.13,1.83,1.83,0,0,0-.88-.28,1,1,0,0,0-1,1.06A1.15,1.15,0,0,0,8,16.53c.85,0,1.35-.35,2.24-1.55l1.49-2,.46,1.88c.23,1,.46,1.66,1.53,1.66s1.66-.75,2.81-2.53l.17-.26-.81-.48-.16.2-.25.34-.19.25c-.45.57-.62.73-.76.73s-.28-.4-.34-.63l-.67-2.83a4.2,4.2,0,0,1-.15-.79C13.84,9.78,14.74,8.22,15.16,8.22Z"></path></svg></md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button toggle="" command="show-files" data-aria-label="Fichiers" title="Fichiers" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fichiers" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->folder</md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div></div>
        <div class="left-pane-bottom"><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button command="snippets" data-aria-label="Extraits de code" title="Extraits de code" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Extraits de code">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->code</md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button command="show-command-palette" data-aria-label="Palette de commandes" title="Palette de commandes" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Palette de commandes">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$-->
      <path d="M21,3H3A2,2,0,0,0,1,5V17a2,2,0,0,0,2,2H21a2,2,0,0,0,2-2V5A2,2,0,0,0,21,3Zm0,2V17H3V5"></path>
      <rect x="5" y="12" width="11" height="2"></rect>
      <rect x="5" y="8" width="11" height="2"></rect>
      <rect x="17" y="8" width="2" height="2"></rect>
      <rect x="17" y="12" width="2" height="2"></rect></svg></md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$846942102$--><md-icon-button command="show-terminal" data-aria-label="Terminal" title="Terminal" value="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Terminal">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->terminal</md-icon>
    </md-icon-button> <!--?lit$846942102$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$846942102$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
        <!--?lit$846942102$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$846942102$--><span class="screenreader-only"><!--?lit$846942102$-->Insérer la cellule de code ci-dessous <!--?lit$846942102$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$846942102$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insérer la cellule de code ci-dessous" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Insérer la cellule de code ci-dessous (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$846942102$-->Code
          </colab-toolbar-button>
          <!--?lit$846942102$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
        <!--?lit$846942102$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$846942102$--><span class="screenreader-only"><!--?lit$846942102$-->Ajouter une cellule de texte <!--?lit$846942102$--></span>
      </md-text-button>
      <!--?lit$846942102$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Ajouter une cellule de texte" shortcut=""><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ajouter une cellule de texte</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$846942102$-->Texte
          </colab-toolbar-button>
        
    <!--?lit$846942102$-->
    <!--?lit$846942102$-->
    <!--?lit$846942102$-->
    <!--?lit$846942102$-->
    <!--?lit$846942102$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true" title=""><template shadowrootmode="open"><!----><button class=" save-message "><!--?lit$846942102$-->Toutes les modifications ont été enregistrées</button></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$846942102$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$846942102$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$846942102$--><!--?lit$846942102$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$846942102$--><!--?-->
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Cliquez pour établir la connexion"><template shadowrootmode="open"><!----><md-text-button id="button" value="" data-aria-disabled="false"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
        <!--?lit$846942102$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$846942102$--><span class="screenreader-only"><!--?lit$846942102$-->Cliquez pour établir la connexion <!--?lit$846942102$--></span>
      </md-text-button>
      <!--?lit$846942102$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Cliquez pour établir la connexion" shortcut=""><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Cliquez pour établir la connexion</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$846942102$-->Reconnecter
      </colab-toolbar-button>
      <!--?lit$846942102$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Options de connexion supplémentaires" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Options de connexion supplémentaires" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Options de connexion supplémentaires"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Options de connexion supplémentaires</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$846942102$--> <span class="colab-separator"></span>
          <colab-toolbar-button command="show-chat" icon="spark"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
        <!--?lit$846942102$-->
    <svg slot="icon" viewBox="0 -960 960 960" width="24" height="24">
      <defs>
        <lineargradient id="sparkGradient" x1="0" y1="1" x2="1" y2="0">
          <stop offset="33.06%" stop-color="#217BFE"></stop>
          <stop offset="44.4%" stop-color="#078EFB"></stop>
          <stop offset="65.69%" stop-color="#A190FF"></stop>
          <stop offset="75.05%" stop-color="#BD99FE"></stop>
        </lineargradient>
      </defs>
      <path fill="url(#sparkGradient)" d="M480-80q2 0 2-2 0-82 31-154t85-126q54-54 126-85t154-31q2 0 2-2t-2-2q-82 0-154-31t-126-85q-54-54-85-126t-31-154q0-2-2-2t-2 2q0 82-31 154t-85 126q-54 54-126 85T82-482q-2 0-2 2t2 2q82 0 154 31t126 85q54 54 85 126t31 154q0 2 2 2Z"></path>
    </svg>
        <span class="button-content"><slot></slot></span>
        <!--?lit$846942102$--><span class="screenreader-only"><!--?lit$846942102$--> <!--?lit$846942102$--></span>
      </md-text-button>
      <!--?lit$846942102$--><!--?--></template>
            <!--?lit$846942102$-->Gemini
          </colab-toolbar-button>
    <!--?lit$846942102$-->
    <span class="collapsed-options">
      <!--?lit$846942102$--><span class="colab-separator"></span>
      <!--?lit$846942102$--> <md-icon-button command="share" title="Partager le notebook" data-aria-label="Partager le notebook" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Partager le notebook">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->people</md-icon>
          </md-icon-button><md-icon-button command="preferences" data-aria-label="Ouvrir les paramètres" title="Ouvrir les paramètres" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Ouvrir les paramètres">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$846942102$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Activer/Désactiver l&#39;affichage de l&#39;en-tête" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Activer/Désactiver l&#39;affichage de l&#39;en-tête" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Activer/Désactiver l'affichage de l'en-tête</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$846942102$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$846942102$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-kXEKxRIjlvWO" class="selected-tab" md-tab="" active="" tabindex="0"><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$846942102$--><div class="indicator"></div>
      </div>
      <!--?lit$846942102$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-kXEKxRIjlvWO"><!--?lit$846942102$--><!--?lit$846942102$-->Notebook<!--?--></span>
            <!--?lit$846942102$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$846942102$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Autres actions liées aux onglets" data-aria-label="Autres actions liées aux onglets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Autres actions liées aux onglets" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" role="main" class="notebook-container" aria-label="Notebook" tabindex="-1">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$846942102$-->
              <div class="notebook-content ">
                <!--?lit$846942102$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Ajouter une cellule de code
Ctrl+M B" title="Ajouter une cellule de code
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de code
Ctrl+M B">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Ajouter une cellule de texte" title="Ajouter une cellule de texte" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de texte">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Texte
        </md-outlined-button>
        <!--?lit$846942102$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell text" id="cell-C2-h6efDl1b1" tabindex="-1" role="region" aria-label="Cellule 0 : Cellule de texte : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p><strong>Installation de bibliothèques nécessaires</strong></p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-Vh7lhw5plvVl" tabindex="-1" role="region" aria-label="Cellule 1 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:20 (il y a 9 heures)
exécuté en 15.147 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:20 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 15.147&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk6">!</span><span class="mtk1">pip&nbsp;install&nbsp;pyspark&nbsp;matplotlib&nbsp;seaborn&nbsp;pandas</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 1" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output_text"><pre>Requirement already satisfied: pyspark in /usr/local/lib/python3.10/dist-packages (3.5.3)
Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (3.8.0)
Requirement already satisfied: seaborn in /usr/local/lib/python3.10/dist-packages (0.13.2)
Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.2.2)
Requirement already satisfied: py4j==0.10.9.7 in /usr/local/lib/python3.10/dist-packages (from pyspark) (0.10.9.7)
Requirement already satisfied: contourpy&gt;=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.3.1)
Requirement already satisfied: cycler&gt;=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools&gt;=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (4.55.0)
Requirement already satisfied: kiwisolver&gt;=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.4.7)
Requirement already satisfied: numpy&lt;2,&gt;=1.21 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (1.26.4)
Requirement already satisfied: packaging&gt;=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (24.2)
Requirement already satisfied: pillow&gt;=6.2.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (11.0.0)
Requirement already satisfied: pyparsing&gt;=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (3.2.0)
Requirement already satisfied: python-dateutil&gt;=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib) (2.8.2)
Requirement already satisfied: pytz&gt;=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)
Requirement already satisfied: tzdata&gt;=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)
Requirement already satisfied: six&gt;=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil&gt;=2.7-&gt;matplotlib) (1.16.0)
</pre></div></div><div></div></colab-static-output-renderer></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code icon-scrolling" id="cell-1naAyC7Hl5vk" tabindex="-1" role="region" aria-label="Cellule 2 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;plt</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;seaborn&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;sns</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;pd</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Assurez-vous&nbsp;que&nbsp;Spark&nbsp;et&nbsp;pandas&nbsp;sont&nbsp;</span><span class="mtk8">correctement&nbsp;configurés</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;pyspark.sql&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;SparkSession</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;pyspark.sql.functions&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;col,&nbsp;avg</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 2" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell--rF8AQhgo7L8" tabindex="-1" role="region" aria-label="Cellule 3 : Cellule de texte : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p><strong>Initialisation de la session Spark</strong></p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code icon-scrolling" id="cell-e7WDFy9ol6j2" tabindex="-1" role="region" aria-label="Cellule 4 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk8">#cette&nbsp;ligne&nbsp;permet&nbsp;de&nbsp;créer&nbsp;ou&nbsp;d'obtenir&nbsp;une&nbsp;</span><span class="mtk8">session&nbsp;Spark&nbsp;pour&nbsp;effectuer&nbsp;des&nbsp;traitements&nbsp;</span><span class="mtk8">distribués&nbsp;sur&nbsp;de&nbsp;BigData</span></span><br><span><span class="mtk1">spark&nbsp;=&nbsp;SparkSession.builder&nbsp;\</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;.appName(</span><span class="mtk26">"Patient&nbsp;Data&nbsp;Analysis"</span><span class="mtk1">)&nbsp;\</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;.getOrCreate()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 4" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-AYjAFaVWo_7r" tabindex="-1" role="region" aria-label="Cellule 5 : Cellule de texte : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p><strong>Téléchargement  des données CSV dans un DataFrame PySpark</strong></p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-40o_W3Hkl6g-" tabindex="-1" role="region" aria-label="Cellule 6 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:36 (il y a 9 heures)
exécuté en 557.126 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:36 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 557.126&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;google.colab&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;files</span></span><br><span><span class="mtk1">uploaded&nbsp;=&nbsp;files.upload()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Charger&nbsp;le&nbsp;fichier&nbsp;CSV&nbsp;dans&nbsp;un&nbsp;DataFrame&nbsp;PySpark</span></span><br><span><span class="mtk1">file_path&nbsp;=&nbsp;</span><span class="mtk14">list</span><span class="mtk1">(uploaded.keys())[</span><span class="mtk12">0</span><span class="mtk1">]&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Récupère&nbsp;le&nbsp;nom&nbsp;du&nbsp;fichier&nbsp;téléchargé</span></span><br><span><span class="mtk1">df&nbsp;=&nbsp;spark.read.csv(file_path,&nbsp;header=</span><span class="mtk6">True</span><span class="mtk1">,&nbsp;inferSchema=</span><span class="mtk6">True</span><span class="mtk1">,&nbsp;sep=</span><span class="mtk26">";"</span><span class="mtk1">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 6" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style="height: 71px;"><div class="outputview" style="height: 54px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe.html" class="" style="height: 54px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-1pJEONRBpEaz" tabindex="-1" role="region" aria-label="Cellule 7 : Cellule de texte : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p>** Nettoyage des données**</p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code icon-scrolling" id="cell-KQCcT9BbmGJ0" tabindex="-1" role="region" aria-label="Cellule 8 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk1">df&nbsp;=&nbsp;df.dropna()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 8" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-SL2QYNGepJVF" tabindex="-1" role="region" aria-label="Cellule 9 : Cellule de texte : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><p><strong>Renommage des colonnes du DataFrame PySpark</strong></p>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code icon-scrolling" id="cell-vakLVTxsl6d8" tabindex="-1" role="region" aria-label="Cellule 10 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
  8
  9
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk1">columns_mapping&nbsp;=&nbsp;{</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"SmokerStatus"</span><span class="mtk1">:&nbsp;</span><span class="mtk26">"Smoking"</span><span class="mtk1">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"HadHeartAttack"</span><span class="mtk1">:&nbsp;</span><span class="mtk26">"HeartDisease"</span><span class="mtk1">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"GeneralHealth"</span><span class="mtk1">:&nbsp;</span><span class="mtk26">"HealthStatus"</span><span class="mtk1">,</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"BMI"</span><span class="mtk1">:&nbsp;</span><span class="mtk26">"BodyMassIndex"</span><span class="mtk1">,</span></span><br><span><span class="mtk1">}</span></span><br><span><span class="mtk19">for</span><span class="mtk1">&nbsp;old_col,&nbsp;new_col&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;columns_mapping.items():</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">if</span><span class="mtk1">&nbsp;old_col&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df.columns:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;df&nbsp;=&nbsp;df.withColumnRenamed(old_col,&nbsp;new_col</span><span class="mtk1">)</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 10" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-gN6YsTVelQ2X" tabindex="-1" role="region" aria-label="Cellule 11 : Cellule de texte : Analyse de la Distribution des Patients"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous Analyse de la Distribution des Patients (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous Analyse de la Distribution des Patients (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous Analyse de la Distribution des Patients (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1><strong>Analyse de la Distribution des Patients</strong></h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-YqQk-vQPlUpK" tabindex="-1" role="region" aria-label="Cellule 12 : Cellule de texte : par sexe"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous par sexe (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous par sexe (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous par sexe (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h3><strong>par sexe</strong></h3></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-Y6yULRihl6au" tabindex="-1" role="region" aria-label="Cellule 13 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:36 (il y a 9 heures)
exécuté en 5.404 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:36 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 5.404&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Exemple&nbsp;1&nbsp;:&nbsp;Distribution&nbsp;des&nbsp;patients&nbsp;par&nbsp;sexe</span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk26">"Sex"</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df.columns:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sex_distribution&nbsp;=&nbsp;df.groupBy(</span><span class="mtk26">"Sex"</span><span class="mtk1">).count().toPandas()&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Convertir&nbsp;en&nbsp;DataFrame&nbsp;Pandas&nbsp;pour&nbsp;visualisation</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Affichage&nbsp;sous&nbsp;forme&nbsp;de&nbsp;tableau</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk26">"Distribution&nbsp;des&nbsp;patients&nbsp;par&nbsp;sexe&nbsp;(tableau)&nbsp;:"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;display(sex_distribution)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Utilisation&nbsp;de&nbsp;display()&nbsp;pour&nbsp;afficher&nbsp;un&nbsp;</span><span class="mtk8">tableau&nbsp;bien&nbsp;formaté&nbsp;dans&nbsp;Colab</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.figure(figsize=(</span><span class="mtk12">8</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1">))</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sns.barplot(x=</span><span class="mtk26">'Sex'</span><span class="mtk1">,&nbsp;y=</span><span class="mtk26">'count'</span><span class="mtk1">,&nbsp;data=sex_distribution)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.title(</span><span class="mtk26">'Distribution&nbsp;des&nbsp;patients&nbsp;par&nbsp;sexe'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.show()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 13" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style="height: 620px;"><div class="outputview" style="height: 677px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(1).html" class="" style="height: 677px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-J5AmuDhPlpep" tabindex="-1" role="region" aria-label="Cellule 14 : Cellule de texte : par HealthStatus"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous par HealthStatus (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous par HealthStatus (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous par HealthStatus (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2><strong>par HealthStatus</strong></h2></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-6kdw0kmtl6XM" tabindex="-1" role="region" aria-label="Cellule 15 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:37 (il y a 9 heures)
exécuté en 4.973 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:37 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 4.973&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
</pre><pre class="monaco-colorized colab colab" data-lang="notebook-python"><span><span class="mtk8">#&nbsp;Exemple&nbsp;2&nbsp;:&nbsp;IMC&nbsp;moyen&nbsp;par&nbsp;condition&nbsp;de&nbsp;santé</span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk26">"HealthStatus"</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df.columns&nbsp;</span><span class="mtk6">and</span><span class="mtk1">&nbsp;</span><span class="mtk26">"BodyMassIndex"</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df.columns:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;imc_moyen&nbsp;=&nbsp;df.groupBy(</span><span class="mtk26">"HealthStatus"</span><span class="mtk1">).agg(avg(</span><span class="mtk26">"BodyMassIndex"</span><span class="mtk1">).alias(</span><span class="mtk26">"IMC_Moyen"</span><span class="mtk1">)).toPandas()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Affichage&nbsp;sous&nbsp;forme&nbsp;de&nbsp;tableau</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk26">"IMC&nbsp;moyen&nbsp;par&nbsp;condition&nbsp;de&nbsp;santé&nbsp;(tableau)&nbsp;:"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;display(imc_moyen)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Affichage&nbsp;en&nbsp;format&nbsp;tableau&nbsp;dans&nbsp;Colab</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.figure(figsize=(</span><span class="mtk12">8</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1">))</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;sns.barplot(x=</span><span class="mtk26">'HealthStatus'</span><span class="mtk1">,&nbsp;y=</span><span class="mtk26">'IMC_Moyen'</span><span class="mtk1">,&nbsp;data=imc_moyen)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.title(</span><span class="mtk26">'IMC&nbsp;moyen&nbsp;par&nbsp;condition&nbsp;de&nbsp;santé'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.xticks(rotation=</span><span class="mtk12">45</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;plt.show()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 15" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style="height: 768px;"><div class="outputview" style="height: 817px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(2).html" class="" style="height: 817px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-2vNxJxF2lxos" tabindex="-1" role="region" aria-label="Cellule 16 : Cellule de texte : par Smoking"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous par Smoking (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous par Smoking (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous par Smoking (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2><strong>par Smoking</strong></h2></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-X-5tPUY0l6Ss" tabindex="-1" role="region" aria-label="Cellule 17 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:37 (il y a 9 heures)
exécuté en 8.293 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:37 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 8.293&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
</pre><pre class="monaco-colorized colab colab colab" data-lang="notebook-python"><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk26">"Smoking"</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df.columns&nbsp;</span><span class="mtk6">and</span><span class="mtk1">&nbsp;</span><span class="mtk26">"HeartDisease"</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;df.columns:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;smoking_statuses&nbsp;=&nbsp;[</span><span class="mtk26">"Never&nbsp;smoked"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Former&nbsp;smoker"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Current&nbsp;smoker&nbsp;-&nbsp;now&nbsp;smokes&nbsp;every&nbsp;day"</span><span class="mtk1">]</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">for</span><span class="mtk1">&nbsp;status&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;smoking_statuses:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smoking_data&nbsp;=&nbsp;df.</span><span class="mtk15">filter</span><span class="mtk1">(col(</span><span class="mtk26">"Smoking"</span><span class="mtk1">)&nbsp;==&nbsp;status).groupBy(</span><span class="mtk26">"HeartDisease"</span><span class="mtk1">).count().toPandas()</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Affichage&nbsp;sous&nbsp;forme&nbsp;de&nbsp;tableau</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk26">"Répartition&nbsp;des&nbsp;maladies&nbsp;cardiaques&nbsp;chez&nbsp;les&nbsp;</span><span class="mtk26">fumeurs&nbsp;:&nbsp;</span><span class="mtk1">{status}</span><span class="mtk26">&nbsp;(tableau)&nbsp;:"</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;display(smoking_data)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Affichage&nbsp;en&nbsp;format&nbsp;tableau&nbsp;dans&nbsp;Colab</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;plt.figure(figsize=(</span><span class="mtk12">8</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1">))</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sns.barplot(x=</span><span class="mtk26">'HeartDisease'</span><span class="mtk1">,&nbsp;y=</span><span class="mtk26">'count'</span><span class="mtk1">,&nbsp;data=smoking_data)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;plt.title(</span><span class="mtk6">f</span><span class="mtk26">'Répartition&nbsp;des&nbsp;maladies&nbsp;cardiaques&nbsp;chez&nbsp;les&nbsp;</span><span class="mtk26">fumeurs:&nbsp;</span><span class="mtk1">{status}</span><span class="mtk26">'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;plt.show()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 17" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 1000px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(3).html" class="" style="height: 1000px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-Y0H8m6mTmPJy" tabindex="-1" role="region" aria-label="Cellule 18 : Cellule de texte : ** Analyse et Modélisation des Données Patients : **"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous ** Analyse et Modélisation des Données Patients : ** (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous ** Analyse et Modélisation des Données Patients : ** (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous ** Analyse et Modélisation des Données Patients : ** (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>** Analyse et Modélisation des Données Patients : **</h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-ZXAZk-XFmVXb" tabindex="-1" role="region" aria-label="Cellule 19 : Cellule de texte : Prédiction de la Hauteur et du Poids en Fonction de l&#39;Âge"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous Prédiction de la Hauteur et du Poids en Fonction de l&#39;Âge (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous Prédiction de la Hauteur et du Poids en Fonction de l&#39;Âge (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous Prédiction de la Hauteur et du Poids en Fonction de l&#39;Âge (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2><strong>Prédiction de la Hauteur et du Poids en Fonction de l'Âge</strong></h2></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-2UZ6ATxml6Jk" tabindex="-1" role="region" aria-label="Cellule 20 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:38 (il y a 9 heures)
exécuté en 17.863 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:38 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 17.863&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
</pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk19">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;pd</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;numpy&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;np</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.model_selection&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;train_test_split</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.linear_model&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;LinearRegression</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.metrics&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;mean_squared_error,&nbsp;r2_score</span></span><br><span><span class="mtk19">import</span><span class="mtk1">&nbsp;matplotlib.pyplot&nbsp;</span><span class="mtk19">as</span><span class="mtk1">&nbsp;plt</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;pyspark.sql&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;SparkSession</span></span><br><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.preprocessing&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;LabelEncoder</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Créez&nbsp;ou&nbsp;utilisez&nbsp;votre&nbsp;session&nbsp;Spark</span></span><br><span><span class="mtk1">spark&nbsp;=&nbsp;SparkSession.builder.appName(</span><span class="mtk26">"BMI&nbsp;Analysis"</span><span class="mtk1">).getOrCreate()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Charger&nbsp;les&nbsp;données&nbsp;depuis&nbsp;un&nbsp;fichier&nbsp;CSV&nbsp;avec&nbsp;</span><span class="mtk8">PySpark</span></span><br><span><span class="mtk1">file_path&nbsp;=&nbsp;</span><span class="mtk26">"PatientsData.csv"</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Remplacez&nbsp;par&nbsp;le&nbsp;chemin&nbsp;de&nbsp;votre&nbsp;fichier</span></span><br><span><span class="mtk1">data&nbsp;=&nbsp;spark.read.csv(file_path,&nbsp;header=</span><span class="mtk6">True</span><span class="mtk1">,&nbsp;inferSchema=</span><span class="mtk6">True</span><span class="mtk1">,&nbsp;sep=</span><span class="mtk26">";"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Vérifier&nbsp;les&nbsp;colonnes&nbsp;nécessaires</span></span><br><span><span class="mtk19">if</span><span class="mtk1">&nbsp;</span><span class="mtk26">"AgeCategory"</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;data.columns&nbsp;</span><span class="mtk6">or</span><span class="mtk1">&nbsp;</span><span class="mtk26">"HeightInMeters"</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;data.columns&nbsp;</span><span class="mtk6">or</span><span class="mtk1">&nbsp;</span><span class="mtk26">"WeightInKilograms"</span><span class="mtk1">&nbsp;</span><span class="mtk6">not</span><span class="mtk1">&nbsp;</span><span class="mtk6">in</span><span class="mtk1">&nbsp;data.columns:</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk19">raise</span><span class="mtk1">&nbsp;</span><span class="mtk14">ValueError</span><span class="mtk1">(</span><span class="mtk26">"Le&nbsp;fichier&nbsp;doit&nbsp;contenir&nbsp;les&nbsp;colonnes&nbsp;'AgeCategor</span><span class="mtk26">y',&nbsp;'HeightInMeters'&nbsp;et&nbsp;'WeightInKilograms'."</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Sélectionner&nbsp;les&nbsp;colonnes&nbsp;du&nbsp;DataFrame&nbsp;PySpark</span></span><br><span><span class="mtk1">X&nbsp;=&nbsp;data.select(</span><span class="mtk26">"AgeCategory"</span><span class="mtk1">)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Variable&nbsp;indépendante</span></span><br><span><span class="mtk1">y_height&nbsp;=&nbsp;data.select(</span><span class="mtk26">"HeightInMeters"</span><span class="mtk1">)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Variable&nbsp;dépendante&nbsp;pour&nbsp;la&nbsp;hauteur</span></span><br><span><span class="mtk1">y_weight&nbsp;=&nbsp;data.select(</span><span class="mtk26">"WeightInKilograms"</span><span class="mtk1">)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Variable&nbsp;dépendante&nbsp;pour&nbsp;le&nbsp;poids</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Convertir&nbsp;le&nbsp;DataFrame&nbsp;PySpark&nbsp;en&nbsp;DataFrame&nbsp;Pand</span><span class="mtk8">as</span></span><br><span><span class="mtk1">X_pandas&nbsp;=&nbsp;X.toPandas()</span></span><br><span><span class="mtk1">y_height_pandas&nbsp;=&nbsp;y_height.toPandas()</span></span><br><span><span class="mtk1">y_weight_pandas&nbsp;=&nbsp;y_weight.toPandas()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Encoder&nbsp;la&nbsp;variable&nbsp;'AgeCategory'&nbsp;en&nbsp;valeurs&nbsp;</span><span class="mtk8">numériques</span></span><br><span><span class="mtk1">label_encoder&nbsp;=&nbsp;LabelEncoder()</span></span><br><span><span class="mtk1">X_pandas[</span><span class="mtk26">"AgeCategory"</span><span class="mtk1">]&nbsp;=&nbsp;label_encoder.fit_transform(X_pandas[</span><span class="mtk26">"AgeCategory"</span><span class="mtk1">])</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Convertir&nbsp;les&nbsp;colonnes&nbsp;de&nbsp;hauteur&nbsp;et&nbsp;de&nbsp;poids&nbsp;en&nbsp;</span><span class="mtk8">type&nbsp;float&nbsp;en&nbsp;remplaçant&nbsp;la&nbsp;virgule&nbsp;par&nbsp;un&nbsp;point</span></span><br><span><span class="mtk1">y_height_pandas&nbsp;=&nbsp;y_height_pandas.replace({</span><span class="mtk26">','</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'.'</span><span class="mtk1">},&nbsp;regex=</span><span class="mtk6">True</span><span class="mtk1">).astype(</span><span class="mtk14">float</span><span class="mtk1">)</span></span><br><span><span class="mtk1">y_weight_pandas&nbsp;=&nbsp;y_weight_pandas.replace({</span><span class="mtk26">','</span><span class="mtk1">:&nbsp;</span><span class="mtk26">'.'</span><span class="mtk1">},&nbsp;regex=</span><span class="mtk6">True</span><span class="mtk1">).astype(</span><span class="mtk14">float</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Séparer&nbsp;les&nbsp;données&nbsp;en&nbsp;ensembles&nbsp;d'entraînement&nbsp;</span><span class="mtk8">et&nbsp;de&nbsp;test</span></span><br><span><span class="mtk1">X_train,&nbsp;X_test,&nbsp;y_height_train,&nbsp;y_height_test&nbsp;=&nbsp;t</span><span class="mtk1">rain_test_split(X_pandas,&nbsp;y_height_pandas,&nbsp;test_si</span><span class="mtk1">ze=</span><span class="mtk12">0.2</span><span class="mtk1">,&nbsp;random_state=</span><span class="mtk12">42</span><span class="mtk1">)</span></span><br><span><span class="mtk1">_,&nbsp;_,&nbsp;y_weight_train,&nbsp;y_weight_test&nbsp;=&nbsp;train_test_s</span><span class="mtk1">plit(X_pandas,&nbsp;y_weight_pandas,&nbsp;test_size=</span><span class="mtk12">0.2</span><span class="mtk1">,&nbsp;random_state=</span><span class="mtk12">42</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Modèles&nbsp;de&nbsp;régression&nbsp;linéaire&nbsp;pour&nbsp;la&nbsp;hauteur&nbsp;</span><span class="mtk8">et&nbsp;le&nbsp;poids</span></span><br><span><span class="mtk1">model_height&nbsp;=&nbsp;LinearRegression()</span></span><br><span><span class="mtk1">model_weight&nbsp;=&nbsp;LinearRegression()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Entraîner&nbsp;les&nbsp;modèles</span></span><br><span><span class="mtk1">model_height.fit(X_train,&nbsp;y_height_train)</span></span><br><span><span class="mtk1">model_weight.fit(X_train,&nbsp;y_weight_train)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Prédictions</span></span><br><span><span class="mtk1">y_height_pred&nbsp;=&nbsp;model_height.predict(X_test)</span></span><br><span><span class="mtk1">y_weight_pred&nbsp;=&nbsp;model_weight.predict(X_test)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Évaluer&nbsp;les&nbsp;modèles</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk26">"Évaluation&nbsp;pour&nbsp;la&nbsp;hauteur&nbsp;:"</span><span class="mtk1">)</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk26">"R2&nbsp;Score&nbsp;:&nbsp;</span><span class="mtk1">{r2_score(y_height_test,&nbsp;y_height_pred)}</span><span class="mtk26">"</span><span class="mtk1">)</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk26">"Erreur&nbsp;quadratique&nbsp;moyenne&nbsp;:&nbsp;</span><span class="mtk1">{mean_squared_error(y_height_test,&nbsp;y_height_pred)}</span><span class="mtk26">\n"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk26">"Évaluation&nbsp;pour&nbsp;le&nbsp;poids&nbsp;:"</span><span class="mtk1">)</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk26">"R2&nbsp;Score&nbsp;:&nbsp;</span><span class="mtk1">{r2_score(y_weight_test,&nbsp;y_weight_pred)}</span><span class="mtk26">"</span><span class="mtk1">)</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk6">f</span><span class="mtk26">"Erreur&nbsp;quadratique&nbsp;moyenne&nbsp;:&nbsp;</span><span class="mtk1">{mean_squared_error(y_weight_test,&nbsp;y_weight_pred)}</span><span class="mtk26">\n"</span><span class="mtk1">)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Visualisation&nbsp;:&nbsp;Prédiction&nbsp;de&nbsp;la&nbsp;hauteur&nbsp;en&nbsp;</span><span class="mtk8">fonction&nbsp;de&nbsp;l'âge</span></span><br><span><span class="mtk1">plt.figure(figsize=(</span><span class="mtk12">12</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1">))</span></span><br><span><span class="mtk1">plt.scatter(X_test,&nbsp;y_height_test,&nbsp;color=</span><span class="mtk26">'blue'</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">'Données&nbsp;réelles'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.plot(X_test,&nbsp;y_height_pred,&nbsp;color=</span><span class="mtk26">'red'</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">'Prédiction'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.title(</span><span class="mtk26">'Prédiction&nbsp;de&nbsp;la&nbsp;Hauteur&nbsp;en&nbsp;fonction&nbsp;de&nbsp;l\'Âge'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.xlabel(</span><span class="mtk26">'Âge'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.ylabel(</span><span class="mtk26">'Hauteur&nbsp;(m)'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.legend()</span></span><br><span><span class="mtk1">plt.grid()</span></span><br><span><span class="mtk1">plt.show()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Visualisation&nbsp;:&nbsp;Prédiction&nbsp;du&nbsp;poids&nbsp;en&nbsp;fonction&nbsp;</span><span class="mtk8">de&nbsp;l'âge</span></span><br><span><span class="mtk1">plt.figure(figsize=(</span><span class="mtk12">12</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1">))</span></span><br><span><span class="mtk1">plt.scatter(X_test,&nbsp;y_weight_test,&nbsp;color=</span><span class="mtk26">'green'</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">'Données&nbsp;réelles'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.plot(X_test,&nbsp;y_weight_pred,&nbsp;color=</span><span class="mtk26">'orange'</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">'Prédiction'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.title(</span><span class="mtk26">'Prédiction&nbsp;du&nbsp;Poids&nbsp;en&nbsp;fonction&nbsp;de&nbsp;l\'Âge'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.xlabel(</span><span class="mtk26">'Âge'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.ylabel(</span><span class="mtk26">'Poids&nbsp;(kg)'</span><span class="mtk1">)</span></span><br><span><span class="mtk1">plt.legend()</span></span><br><span><span class="mtk1">plt.grid()</span></span><br><span><span class="mtk1">plt.show()</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Faire&nbsp;des&nbsp;prédictions&nbsp;pour&nbsp;de&nbsp;nouveaux&nbsp;âges</span></span><br><span><span class="mtk1">new_ages&nbsp;=&nbsp;np.array([</span><span class="mtk12">20</span><span class="mtk1">,&nbsp;</span><span class="mtk12">30</span><span class="mtk1">,&nbsp;</span><span class="mtk12">40</span><span class="mtk1">,&nbsp;</span><span class="mtk12">50</span><span class="mtk1">]).reshape(</span><span class="mtk12">-1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">)&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Exemple&nbsp;d'âges&nbsp;pour&nbsp;prédiction</span></span><br><span><span class="mtk1">predicted_heights&nbsp;=&nbsp;model_height.predict(new_ages)</span></span><br><span><span class="mtk1">predicted_weights&nbsp;=&nbsp;model_weight.predict(new_ages)</span></span><br><span><span></span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Afficher&nbsp;les&nbsp;prédictions</span></span><br><span><span class="mtk1">predictions&nbsp;=&nbsp;pd.DataFrame({</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"Age"</span><span class="mtk1">:&nbsp;new_ages.flatten(),&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;aplatir&nbsp;le&nbsp;tableau</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"Predicted_HeightInMeters"</span><span class="mtk1">:&nbsp;predicted_heights.flatten(),&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;aplatir&nbsp;le&nbsp;tableau</span></span><br><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"Predicted_WeightInKilograms"</span><span class="mtk1">:&nbsp;predicted_weights.flatten()&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;aplatir&nbsp;le&nbsp;tableau</span></span><br><span><span class="mtk1">})</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk26">"Prédictions&nbsp;pour&nbsp;de&nbsp;nouveaux&nbsp;âges&nbsp;:"</span><span class="mtk1">)</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(predictions)</span></span><br><span><span></span></span><br><span><span class="mtk8">#&nbsp;Sauvegarder&nbsp;les&nbsp;prédictions&nbsp;dans&nbsp;un&nbsp;fichier&nbsp;CSV</span></span><br><span><span class="mtk1">predictions.to_csv(</span><span class="mtk26">"predictions.csv"</span><span class="mtk1">,&nbsp;index=</span><span class="mtk6">False</span><span class="mtk1">)</span></span><br><span><span class="mtk15">print</span><span class="mtk1">(</span><span class="mtk26">"Les&nbsp;prédictions&nbsp;ont&nbsp;été&nbsp;enregistrées&nbsp;dans&nbsp;</span><span class="mtk26">'predictions.csv'."</span><span class="mtk1">)</span></span><br><span><span></span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 20" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 1000px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(4).html" class="" style="height: 1000px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-hyN6U5FSpzOH" tabindex="-1" role="region" aria-label="Cellule 21 : Cellule de texte : *Prédiction de la Réalisation de Tests COVID-19 Basée sur le Nombre de Tests VIH : *"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous *Prédiction de la Réalisation de Tests COVID-19 Basée sur le Nombre de Tests VIH : * (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous *Prédiction de la Réalisation de Tests COVID-19 Basée sur le Nombre de Tests VIH : * (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous *Prédiction de la Réalisation de Tests COVID-19 Basée sur le Nombre de Tests VIH : * (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>*<em>Prédiction de la Réalisation de Tests COVID-19 Basée sur le Nombre de Tests VIH : *</em></h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution ">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-QtZ-bCpop1mP" tabindex="-1" role="region" aria-label="Cellule 22 : Cellule de texte : Modélisation avec Régression Logistique"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous Modélisation avec Régression Logistique (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous Modélisation avec Régression Logistique (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous Modélisation avec Régression Logistique (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2><strong>Modélisation avec Régression Logistique</strong></h2></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code code-has-output icon-scrolling focused" id="cell-EdN6CbYFl6HE" tabindex="-1" role="region" aria-label="Cellule 23 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----> <md-icon-button class="colab-icon" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Déplacer la cellule vers le haut
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Déplacer la cellule vers le haut
Ctrl+M K">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->arrow_upward</md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Déplacer la cellule vers le haut
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Déplacer la cellule vers le haut</div><!----><!----><div><!--?lit$846942102$-->Ctrl+M K</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Déplacer la cellule vers le bas
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Déplacer la cellule vers le bas
Ctrl+M J">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->arrow_downward</md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Déplacer la cellule vers le bas
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Déplacer la cellule vers le bas</div><!----><!----><div><!--?lit$846942102$-->Ctrl+M J</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----><!--?lit$846942102$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-EdN6CbYFl6HE" anchor="ai-menu-anchor-EdN6CbYFl6HE" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$846942102$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$846942102$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$846942102$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$846942102$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$846942102$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$846942102$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$846942102$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$846942102$-->Générer un code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$846942102$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$846942102$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$846942102$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$846942102$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$846942102$-->Expliquer le code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button class="colab-icon" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-EdN6CbYFl6HE-tooltip" data-aria-label="Fonctionnalités d&#39;IA disponibles" id="ai-menu-anchor-EdN6CbYFl6HE" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fonctionnalités d&#39;IA disponibles" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-EdN6CbYFl6HE" id="ai-menu-anchor-EdN6CbYFl6HE-tooltip" message="Fonctionnalités d&#39;IA disponibles"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Fonctionnalités d'IA disponibles</div><!----><!--?--></template>
              </colab-tooltip-trigger> <!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copier le lien dans la cellule" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copier le lien dans la cellule">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->link</md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copier le lien dans la cellule"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Copier le lien dans la cellule</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-add-comment-tooltip" data-aria-label="Ajouter un commentaire
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Ajouter un commentaire
Ctrl+Alt+M">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->comment</md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Ajouter un commentaire
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ajouter un commentaire</div><!----><!----><div><!--?lit$846942102$-->Ctrl+Alt+M</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Ouvrir les paramètres de l&#39;éditeur" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Ouvrir les paramètres de l&#39;éditeur">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->settings</md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Ouvrir les paramètres de l&#39;éditeur"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Ouvrir les paramètres de l'éditeur</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Modifier" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Modifier" aria-pressed="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->edit</md-icon>
            <!--?lit$846942102$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->edit_off</md-icon>
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Modifier"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Modifier</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mettre en miroir la cellule dans un onglet" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mettre en miroir la cellule dans un onglet">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mettre en miroir la cellule dans un onglet"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Mettre en miroir la cellule dans un onglet</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!----> <md-icon-button class="colab-icon" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Supprimer la cellule
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Supprimer la cellule
Ctrl+M D">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->delete</md-icon>
            <!--?lit$846942102$-->
          </md-icon-button>
          <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Supprimer la cellule
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Supprimer la cellule</div><!----><!----><div><!--?lit$846942102$-->Ctrl+M D</div><!----><!--?--></template>
              </colab-tooltip-trigger><!--?--><!----><!--?lit$846942102$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="Plus d&#39;actions relatives à la cellule" class="colab-icon cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Plus d&#39;actions relatives à la cellule" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="Plus d&#39;actions relatives à la cellule"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Plus d'actions relatives à la cellule</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:38 (il y a 9 heures)
exécuté en 0.954 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:38 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 0.954&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="385" data-mode-id="notebook-python" style="height: 979px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/610" style="width: 1573px; height: 979px;"><div data-mprt="3" class="overflow-guard" style="width: 1573px; height: 979px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 979px; width: 29px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 979px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 29px; height: 979px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:29px; height:19px;"></div><div class="line-numbers active-line-number" style="left:0px;width:23px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">3</div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">4</div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">5</div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">6</div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">7</div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">8</div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">9</div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">10</div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">11</div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">12</div></div><div style="position:absolute;top:228px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">13</div></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">14</div></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">15</div></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">16</div></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">17</div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">18</div></div><div style="position:absolute;top:342px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">19</div></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">20</div></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">21</div></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">22</div></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">23</div></div><div style="position:absolute;top:437px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">24</div></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">25</div></div><div style="position:absolute;top:475px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">26</div></div><div style="position:absolute;top:494px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">27</div></div><div style="position:absolute;top:513px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">28</div></div><div style="position:absolute;top:532px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">29</div></div><div style="position:absolute;top:551px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">30</div></div><div style="position:absolute;top:570px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">31</div></div><div style="position:absolute;top:589px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">32</div></div><div style="position:absolute;top:608px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">33</div></div><div style="position:absolute;top:627px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">34</div></div><div style="position:absolute;top:646px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">35</div></div><div style="position:absolute;top:665px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">36</div></div><div style="position:absolute;top:684px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">37</div></div><div style="position:absolute;top:703px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">38</div></div><div style="position:absolute;top:722px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">39</div></div><div style="position:absolute;top:741px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">40</div></div><div style="position:absolute;top:760px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">41</div></div><div style="position:absolute;top:779px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">42</div></div><div style="position:absolute;top:798px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">43</div></div><div style="position:absolute;top:817px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">44</div></div><div style="position:absolute;top:836px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">45</div></div><div style="position:absolute;top:855px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">46</div></div><div style="position:absolute;top:874px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">47</div></div><div style="position:absolute;top:893px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">48</div></div><div style="position:absolute;top:912px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">49</div></div><div style="position:absolute;top:931px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">50</div></div><div style="position:absolute;top:950px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">51</div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 29px; width: 1544px; height: 979px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 979px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1544px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1544px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div><div style="position:absolute;top:950px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 979px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1544px; height: 979px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.linear_model&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;LogisticRegression</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span class="mtk19">from</span><span class="mtk1">&nbsp;sklearn.metrics&nbsp;</span><span class="mtk19">import</span><span class="mtk1">&nbsp;accuracy_score,&nbsp;confusion_matrix</span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Exemple&nbsp;de&nbsp;données</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Supposons&nbsp;que&nbsp;nous&nbsp;avons&nbsp;les&nbsp;années,&nbsp;les&nbsp;tests&nbsp;</span><span class="mtk8">VIH&nbsp;effectués&nbsp;et&nbsp;si&nbsp;un&nbsp;test&nbsp;COVID&nbsp;a&nbsp;été&nbsp;effectué&nbsp;</span><span class="mtk8">(0&nbsp;ou&nbsp;1)</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1">data&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"Year"</span><span class="mtk1">:&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">2019</span><span class="mtk1">,&nbsp;</span><span class="mtk12">2020</span><span class="mtk1">,&nbsp;</span><span class="mtk12">2021</span><span class="mtk1">,&nbsp;</span><span class="mtk12">2022</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"HIV_Tests_Conducted"</span><span class="mtk1">:&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">500000</span><span class="mtk1">,&nbsp;</span><span class="mtk12">350000</span><span class="mtk1">,&nbsp;</span><span class="mtk12">400000</span><span class="mtk1">,&nbsp;</span><span class="mtk12">450000</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Nombre&nbsp;de&nbsp;tests&nbsp;VIH&nbsp;réalisés</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"COVID_Tested"</span><span class="mtk1">:&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;0&nbsp;=&nbsp;Aucun&nbsp;test&nbsp;COVID,&nbsp;1&nbsp;=&nbsp;Test&nbsp;COVID&nbsp;effectué</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk1 bracket-highlighting-0">}</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Créer&nbsp;un&nbsp;DataFrame&nbsp;Pandas</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">data</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Caractéristiques&nbsp;(variables&nbsp;indépendantes)</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;df</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"HIV_Tests_Conducted"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Nous&nbsp;allons&nbsp;utiliser&nbsp;le&nbsp;nombre&nbsp;de&nbsp;tests&nbsp;VIH&nbsp;</span><span class="mtk8">effectués&nbsp;pour&nbsp;prédire&nbsp;la&nbsp;probabilité&nbsp;d'un&nbsp;test&nbsp;</span><span class="mtk8">COVID</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Variable&nbsp;cible&nbsp;(si&nbsp;un&nbsp;test&nbsp;COVID&nbsp;a&nbsp;été&nbsp;effectué)</span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">y&nbsp;=&nbsp;df</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk26">"COVID_Tested"</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Diviser&nbsp;les&nbsp;données&nbsp;en&nbsp;ensembles&nbsp;d'entraînement&nbsp;</span><span class="mtk8">et&nbsp;de&nbsp;test</span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">X_train,&nbsp;X_test,&nbsp;y_train,&nbsp;y_test&nbsp;=&nbsp;train_test_spli</span><span class="mtk1">t</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X,&nbsp;y,&nbsp;test_size=</span><span class="mtk12">0.2</span><span class="mtk1">,&nbsp;random_state=</span><span class="mtk12">42</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Créer&nbsp;et&nbsp;entraîner&nbsp;le&nbsp;modèle&nbsp;de&nbsp;régression&nbsp;</span><span class="mtk8">logistique</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">model&nbsp;=&nbsp;LogisticRegression</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">model.fit</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X_train,&nbsp;y_train</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Prédire&nbsp;les&nbsp;valeurs&nbsp;sur&nbsp;l'ensemble&nbsp;de&nbsp;test</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk1">y_pred&nbsp;=&nbsp;model.predict</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X_test</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Évaluer&nbsp;le&nbsp;modèle</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">accuracy&nbsp;=&nbsp;accuracy_score</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">y_test,&nbsp;y_pred</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk26">"Précision&nbsp;du&nbsp;modèle&nbsp;:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">accuracy</span><span class="mtk12">:.2f</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk26">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Matrice&nbsp;de&nbsp;confusion</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk1">cm&nbsp;=&nbsp;confusion_matrix</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">y_test,&nbsp;y_pred</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">sns.heatmap</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">cm,&nbsp;annot=</span><span class="mtk6">True</span><span class="mtk1">,&nbsp;fmt=</span><span class="mtk26">"d"</span><span class="mtk1">,&nbsp;cmap=</span><span class="mtk26">"Blues"</span><span class="mtk1">,&nbsp;xticklabels=</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Non"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Oui"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;yticklabels=</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Non"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Oui"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Matrice&nbsp;de&nbsp;confusion"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">plt.xlabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Prédictions"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span class="mtk1">plt.ylabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Véritables"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span class="mtk1">plt.show</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Visualisation&nbsp;des&nbsp;prédictions</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk1">plt.figure</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">figsize=</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk12">8</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk1">plt.scatter</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"HIV_Tests_Conducted"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;df</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"COVID_Tested"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;color=</span><span class="mtk26">"blue"</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">"Données&nbsp;réelles"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk1">plt.plot</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"HIV_Tests_Conducted"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;model.predict</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">df</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk1 bracket-highlighting-3">[</span><span class="mtk26">"HIV_Tests_Conducted"</span><span class="mtk1 bracket-highlighting-3">]</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,&nbsp;color=</span><span class="mtk26">"red"</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">"Prédiction"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Prédiction&nbsp;des&nbsp;tests&nbsp;COVID-19&nbsp;en&nbsp;fonction&nbsp;des&nbsp;</span><span class="mtk26">tests&nbsp;VIH"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span class="mtk1">plt.xlabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Tests&nbsp;VIH"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk1">plt.ylabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Tests&nbsp;COVID&nbsp;(0=Non,&nbsp;1=Oui)"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span class="mtk1">plt.legend</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:950px;height:19px;" class="view-line"><span><span class="mtk1">plt.show</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.25px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1530px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1530px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="11" height="783" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 979px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 979px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 979px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1573px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 29px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover line-numbers" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1573px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 979px;"><div class="minimap-shadow-hidden" style="height: 979px;"></div><canvas width="0" height="783" style="position: absolute; left: 0px; width: 0px; height: 979px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="783" style="position: absolute; left: 0px; width: 0px; height: 979px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1508px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 1038.18px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 23" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 1000px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(5).html" class="" style="height: 1000px;"></iframe></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Ajouter une cellule de code
Ctrl+M B" title="Ajouter une cellule de code
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de code
Ctrl+M B">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Ajouter une cellule de texte" title="Ajouter une cellule de texte" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de texte">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Texte
        </md-outlined-button>
        <!--?lit$846942102$-->
      </div><hr>
    </div></div><div class="cell text" id="cell-jo-XnNqtqF5T" tabindex="-1" role="region" aria-label="Cellule 24 : Cellule de texte : *Analyse et Prédiction des Difficultés à Marcher en Fonction de l&#39;Arthrite et de l&#39;Âge : *"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous *Analyse et Prédiction des Difficultés à Marcher en Fonction de l&#39;Arthrite et de l&#39;Âge : * (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous *Analyse et Prédiction des Difficultés à Marcher en Fonction de l&#39;Arthrite et de l&#39;Âge : * (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous *Analyse et Prédiction des Difficultés à Marcher en Fonction de l&#39;Arthrite et de l&#39;Âge : * (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1>*<em>Analyse et Prédiction des Difficultés à Marcher en Fonction de l'Arthrite et de l'Âge : *</em></h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell text" id="cell-qbVEcBagqLxC" tabindex="-1" role="region" aria-label="Cellule 25 : Cellule de texte : Approche par Régression Logistique"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous Approche par Régression Logistique (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous Approche par Régression Logistique (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous Approche par Régression Logistique (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h2><strong>Approche par Régression Logistique</strong></h2></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Ajouter une cellule de code
Ctrl+M B" title="Ajouter une cellule de code
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de code
Ctrl+M B">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Ajouter une cellule de texte" title="Ajouter une cellule de texte" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de texte">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Texte
        </md-outlined-button>
        <!--?lit$846942102$-->
      </div><hr>
    </div></div><div class="cell code code-has-output icon-scrolling" id="cell-SChLaxwNl6EV" tabindex="-1" role="region" aria-label="Cellule 26 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session

exécuté par Rimah Ben0
23:38 (il y a 9 heures)
exécuté en 1.067 s"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!----><br><!----><!----><div><!--?lit$846942102$-->exécuté par&nbsp;Rimah Ben0</div><!----><!----><div><!--?lit$846942102$-->23:38 (il y a 9 heures)</div><!----><!----><div><!--?lit$846942102$-->exécuté en 1.067&nbsp;s</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="395" data-mode-id="notebook-python" style="height: 960px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs" role="code" data-uri="inmemory://model/613" style="width: 1573px; height: 960px;"><div data-mprt="3" class="overflow-guard" style="width: 1573px; height: 960px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 960px; width: 29px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 960px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 29px; height: 960px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:29px; height:19px;"></div><div class="line-numbers active-line-number" style="left:0px;width:23px;">1</div></div><div style="position:absolute;top:19px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">2</div></div><div style="position:absolute;top:38px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">3</div></div><div style="position:absolute;top:57px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">4</div></div><div style="position:absolute;top:76px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">5</div></div><div style="position:absolute;top:95px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">6</div></div><div style="position:absolute;top:114px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">7</div></div><div style="position:absolute;top:133px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">8</div></div><div style="position:absolute;top:152px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">9</div></div><div style="position:absolute;top:171px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">10</div></div><div style="position:absolute;top:190px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">11</div></div><div style="position:absolute;top:209px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">12</div></div><div style="position:absolute;top:228px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">13</div></div><div style="position:absolute;top:247px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">14</div></div><div style="position:absolute;top:266px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">15</div></div><div style="position:absolute;top:285px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">16</div></div><div style="position:absolute;top:304px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">17</div></div><div style="position:absolute;top:323px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">18</div></div><div style="position:absolute;top:342px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">19</div></div><div style="position:absolute;top:361px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">20</div></div><div style="position:absolute;top:380px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">21</div></div><div style="position:absolute;top:399px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">22</div></div><div style="position:absolute;top:418px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">23</div></div><div style="position:absolute;top:437px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">24</div></div><div style="position:absolute;top:456px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">25</div></div><div style="position:absolute;top:475px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">26</div></div><div style="position:absolute;top:494px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">27</div></div><div style="position:absolute;top:513px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">28</div></div><div style="position:absolute;top:532px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">29</div></div><div style="position:absolute;top:551px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">30</div></div><div style="position:absolute;top:570px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">31</div></div><div style="position:absolute;top:589px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">32</div></div><div style="position:absolute;top:608px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">33</div></div><div style="position:absolute;top:627px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">34</div></div><div style="position:absolute;top:646px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">35</div></div><div style="position:absolute;top:665px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">36</div></div><div style="position:absolute;top:684px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">37</div></div><div style="position:absolute;top:703px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">38</div></div><div style="position:absolute;top:722px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">39</div></div><div style="position:absolute;top:741px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">40</div></div><div style="position:absolute;top:760px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">41</div></div><div style="position:absolute;top:779px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">42</div></div><div style="position:absolute;top:798px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">43</div></div><div style="position:absolute;top:817px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">44</div></div><div style="position:absolute;top:836px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">45</div></div><div style="position:absolute;top:855px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">46</div></div><div style="position:absolute;top:874px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">47</div></div><div style="position:absolute;top:893px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">48</div></div><div style="position:absolute;top:912px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">49</div></div><div style="position:absolute;top:931px;width:100%;height:19px;"><div class="line-numbers" style="left:0px;width:23px;">50</div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 29px; width: 1544px; height: 960px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 960px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1544px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1544px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div><div style="position:absolute;top:627px;width:100%;height:19px;"></div><div style="position:absolute;top:646px;width:100%;height:19px;"></div><div style="position:absolute;top:665px;width:100%;height:19px;"></div><div style="position:absolute;top:684px;width:100%;height:19px;"></div><div style="position:absolute;top:703px;width:100%;height:19px;"></div><div style="position:absolute;top:722px;width:100%;height:19px;"></div><div style="position:absolute;top:741px;width:100%;height:19px;"></div><div style="position:absolute;top:760px;width:100%;height:19px;"></div><div style="position:absolute;top:779px;width:100%;height:19px;"></div><div style="position:absolute;top:798px;width:100%;height:19px;"></div><div style="position:absolute;top:817px;width:100%;height:19px;"></div><div style="position:absolute;top:836px;width:100%;height:19px;"></div><div style="position:absolute;top:855px;width:100%;height:19px;"></div><div style="position:absolute;top:874px;width:100%;height:19px;"></div><div style="position:absolute;top:893px;width:100%;height:19px;"></div><div style="position:absolute;top:912px;width:100%;height:19px;"></div><div style="position:absolute;top:931px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 960px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1544px; height: 960px;"><div style="top:0px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Exemple&nbsp;de&nbsp;données&nbsp;(remplacez-les&nbsp;par&nbsp;vos&nbsp;</span><span class="mtk8">données&nbsp;réelles)</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">data&nbsp;=&nbsp;</span><span class="mtk1 bracket-highlighting-0">{</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"Arthritis"</span><span class="mtk1">:&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;1&nbsp;=&nbsp;Aucune&nbsp;arthrite,&nbsp;0&nbsp;=&nbsp;Avec&nbsp;arthrite</span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"Age"</span><span class="mtk1">:&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">65</span><span class="mtk1">,&nbsp;</span><span class="mtk12">45</span><span class="mtk1">,&nbsp;</span><span class="mtk12">70</span><span class="mtk1">,&nbsp;</span><span class="mtk12">38</span><span class="mtk1">,&nbsp;</span><span class="mtk12">80</span><span class="mtk1">,&nbsp;</span><span class="mtk12">30</span><span class="mtk1">,&nbsp;</span><span class="mtk12">85</span><span class="mtk1">,&nbsp;</span><span class="mtk12">60</span><span class="mtk1">,&nbsp;</span><span class="mtk12">75</span><span class="mtk1">,&nbsp;</span><span class="mtk12">40</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Âge&nbsp;des&nbsp;patients</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk26">"DifficultyWalking"</span><span class="mtk1">:&nbsp;</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1">,&nbsp;</span><span class="mtk12">1</span><span class="mtk1">,&nbsp;</span><span class="mtk12">0</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;1&nbsp;=&nbsp;Difficulté&nbsp;à&nbsp;marcher,&nbsp;0&nbsp;=&nbsp;Pas&nbsp;de&nbsp;difficulté</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1 bracket-highlighting-0">}</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Créer&nbsp;un&nbsp;DataFrame&nbsp;Pandas</span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">df&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">data</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Caractéristiques&nbsp;(variables&nbsp;indépendantes)</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span class="mtk1">X&nbsp;=&nbsp;df</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Arthritis"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Age"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Utilisation&nbsp;de&nbsp;l'arthrite&nbsp;et&nbsp;de&nbsp;l'âge&nbsp;pour&nbsp;</span><span class="mtk8">prédire&nbsp;la&nbsp;difficulté&nbsp;à&nbsp;marcher</span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Variable&nbsp;cible&nbsp;(si&nbsp;la&nbsp;personne&nbsp;a&nbsp;des&nbsp;difficultés&nbsp;</span><span class="mtk8">à&nbsp;marcher)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">y&nbsp;=&nbsp;df</span><span class="mtk1 bracket-highlighting-0">[</span><span class="mtk26">"DifficultyWalking"</span><span class="mtk1 bracket-highlighting-0">]</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Diviser&nbsp;les&nbsp;données&nbsp;en&nbsp;ensembles&nbsp;d'entraînement&nbsp;</span><span class="mtk8">et&nbsp;de&nbsp;test</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">X_train,&nbsp;X_test,&nbsp;y_train,&nbsp;y_test&nbsp;=&nbsp;train_test_spli</span><span class="mtk1">t</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X,&nbsp;y,&nbsp;test_size=</span><span class="mtk12">0.2</span><span class="mtk1">,&nbsp;random_state=</span><span class="mtk12">42</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Créer&nbsp;et&nbsp;entraîner&nbsp;le&nbsp;modèle&nbsp;de&nbsp;régression&nbsp;</span><span class="mtk8">logistique</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">model&nbsp;=&nbsp;LogisticRegression</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">model.fit</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X_train,&nbsp;y_train</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Prédire&nbsp;les&nbsp;valeurs&nbsp;sur&nbsp;l'ensemble&nbsp;de&nbsp;test</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">y_pred&nbsp;=&nbsp;model.predict</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">X_test</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Évaluer&nbsp;le&nbsp;modèle</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk1">accuracy&nbsp;=&nbsp;accuracy_score</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">y_test,&nbsp;y_pred</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk15">print</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk6">f</span><span class="mtk26">"Précision&nbsp;du&nbsp;modèle&nbsp;:&nbsp;</span><span class="mtk1 bracket-highlighting-1">{</span><span class="mtk1">accuracy</span><span class="mtk12">:.2f</span><span class="mtk1 bracket-highlighting-1">}</span><span class="mtk26">"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Matrice&nbsp;de&nbsp;confusion</span></span></div><div style="top:627px;height:19px;" class="view-line"><span><span class="mtk1">cm&nbsp;=&nbsp;confusion_matrix</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">y_test,&nbsp;y_pred</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:646px;height:19px;" class="view-line"><span><span class="mtk1">sns.heatmap</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">cm,&nbsp;annot=</span><span class="mtk6">True</span><span class="mtk1">,&nbsp;fmt=</span><span class="mtk26">"d"</span><span class="mtk1">,&nbsp;cmap=</span><span class="mtk26">"Blues"</span><span class="mtk1">,&nbsp;xticklabels=</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Non"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Oui"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;yticklabels=</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Non"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Oui"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:665px;height:19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Matrice&nbsp;de&nbsp;confusion"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:684px;height:19px;" class="view-line"><span><span class="mtk1">plt.xlabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Prédictions"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:703px;height:19px;" class="view-line"><span><span class="mtk1">plt.ylabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Véritables"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:722px;height:19px;" class="view-line"><span><span class="mtk1">plt.show</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:741px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:760px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Visualisation&nbsp;des&nbsp;prédictions</span></span></div><div style="top:779px;height:19px;" class="view-line"><span><span class="mtk1">plt.figure</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">figsize=</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk12">8</span><span class="mtk1">,&nbsp;</span><span class="mtk12">6</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:798px;height:19px;" class="view-line"><span><span class="mtk1">plt.scatter</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Age"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;df</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"DifficultyWalking"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;color=</span><span class="mtk26">"blue"</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">"Données&nbsp;réelles"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:817px;height:19px;" class="view-line"><span><span class="mtk1">plt.plot</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk1 bracket-highlighting-1">[</span><span class="mtk26">"Age"</span><span class="mtk1 bracket-highlighting-1">]</span><span class="mtk1">,&nbsp;model.predict</span><span class="mtk1 bracket-highlighting-1">(</span><span class="mtk1">df</span><span class="mtk1 bracket-highlighting-2">[</span><span class="mtk1 bracket-highlighting-3">[</span><span class="mtk26">"Arthritis"</span><span class="mtk1">,&nbsp;</span><span class="mtk26">"Age"</span><span class="mtk1 bracket-highlighting-3">]</span><span class="mtk1 bracket-highlighting-2">]</span><span class="mtk1 bracket-highlighting-1">)</span><span class="mtk1">,&nbsp;color=</span><span class="mtk26">"red"</span><span class="mtk1">,&nbsp;label=</span><span class="mtk26">"Prédiction"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:836px;height:19px;" class="view-line"><span><span class="mtk1">plt.title</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Prédiction&nbsp;de&nbsp;la&nbsp;difficulté&nbsp;à&nbsp;marcher&nbsp;en&nbsp;fonction&nbsp;</span><span class="mtk26">de&nbsp;l'arthrite&nbsp;et&nbsp;de&nbsp;l'âge"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:855px;height:19px;" class="view-line"><span><span class="mtk1">plt.xlabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Âge"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:874px;height:19px;" class="view-line"><span><span class="mtk1">plt.ylabel</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk26">"Difficulté&nbsp;à&nbsp;marcher&nbsp;(0=Non,&nbsp;1=Oui)"</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:893px;height:19px;" class="view-line"><span><span class="mtk1">plt.legend</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:912px;height:19px;" class="view-line"><span><span class="mtk1">plt.show</span><span class="mtk1 bracket-highlighting-0">(</span><span class="mtk1 bracket-highlighting-0">)</span></span></div><div style="top:931px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 1.25px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1530px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1530px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="11" height="768" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 960px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 960px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 960px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1573px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 29px; width: 76992px; height: 1px;"></textarea><div class="monaco-editor-background textAreaCover line-numbers" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1573px;"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 960px;"><div class="minimap-shadow-hidden" style="height: 960px;"></div><canvas width="0" height="768" style="position: absolute; left: 0px; width: 0px; height: 960px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="768" style="position: absolute; left: 0px; width: 0px; height: 960px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1697px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 1038.18px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 26" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Actions sur la sortie des cellules de code" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Actions sur la sortie des cellules de code" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <!--?lit$846942102$--><colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Actions sur la sortie des cellules de code"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Actions sur la sortie des cellules de code</div><!----><!--?--></template></colab-tooltip-trigger><!--?--></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div style=""><div class="outputview" style="height: 1000px;"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(6).html" class="" style="height: 1000px;"></iframe></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Ajouter une cellule de code
Ctrl+M B" title="Ajouter une cellule de code
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de code
Ctrl+M B">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Ajouter une cellule de texte" title="Ajouter une cellule de texte" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button" aria-label="Ajouter une cellule de texte">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$846942102$-->Texte
        </md-outlined-button>
        <!--?lit$846942102$-->
      </div><hr>
    </div></div><div class="cell text" id="cell-pZEU67jPr2OW" tabindex="-1" role="region" aria-label="Cellule 27 : Cellule de texte : Clôturer SparkSession"><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><!----> <div class="toolbar-root"></div>
      <div class="editor-container horizontal">
        <div class="editor-root"></div>
        <div class="text-top-div">
          <div class="markdown"><span><div class="text-cell-section-header layout horizontal center"><md-icon-button class="header-section-toggle" title="Réduire 0 cellule enfant sous Clôturer SparkSession (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" data-aria-label="Réduire 0 cellule enfant sous Clôturer SparkSession (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Réduire 0 cellule enfant sous Clôturer SparkSession (appuyez sur &lt;Maj&gt; pour réduire aussi les sections dépendantes)">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>keyboard_arrow_down</md-icon></md-icon-button><h1><strong>Clôturer SparkSession</strong></h1></div>
</span></div>
        </div>
      </div>

      <div class="section-header" style="display: none;">
        <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution">
      <button id="run-button" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
        <div class="section-header-container" title="cliquer pour développer">↳ 0&nbsp;cellule masquée</div>
      </div></div></div><div class="add-cell">
      <hr>
    </div></div><div class="cell code icon-scrolling" id="cell-ptKuTEqTm2Ee" tabindex="-1" role="region" aria-label="Cellule 28 : Cellule de code : "><div class="cell-tag-editor sticky"></div><div class="cell-toolbar sticky"></div><div class="main-content" elevation="0"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class=" cell-execution stale ">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Exécuter la cellule">
        <span class="execution-count"><!--?lit$846942102$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$846942102$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$846942102$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$846942102$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Exécuter la cellule (Ctrl+Enter)
cellule non exécutée au cours de cette session"><template shadowrootmode="open"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Exécuter la cellule (Ctrl+Enter)</div><!----><!----><div><!--?lit$846942102$-->cellule non exécutée au cours de cette session</div><!----><!--?--></template>
    </colab-tooltip-trigger> <!--?lit$846942102$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><pre class="lazy-virtualized" style="font-size: 14px; line-height: 19px;"><pre class="lazy-gutter">  1
</pre><pre class="monaco-colorized colab colab colab colab" data-lang="notebook-python"><span><span class="mtk1">spark.stop()</span></span><br></pre><colab-read-only-cell-placeholder style="display: none;"><template shadowrootmode="open"><!----><div><!--?lit$846942102$-->Commencez à coder ou à <span tabindex="0" role="button" class="link">générer</span> avec l'IA.</div></template></colab-read-only-cell-placeholder></pre></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Sortie de la cellule 28" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> </div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Commentaires" style="display: none;"></section></div>
          <!--?lit$846942102$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links&amp;authuser=1">
        <!--?lit$846942102$-->Produits payants Colab
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$846942102$-->Résilier les contrats ici
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$846942102$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$846942102$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Autres actions liées aux onglets" data-aria-label="Autres actions liées aux onglets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Autres actions liées aux onglets" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$846942102$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$846942102$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$846942102$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Autres actions liées aux onglets" data-aria-label="Autres actions liées aux onglets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Autres actions liées aux onglets" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 33.3%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$846942102$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$846942102$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="Autres actions liées aux onglets" data-aria-label="Autres actions liées aux onglets" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Autres actions liées aux onglets" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(7).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals allow-popups-to-escape-sandbox" src="./Analyse de données_files/outputframe(8).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Barre d&#39;état de l&#39;environnement d&#39;exécution" style="min-height: inherit;"><template shadowrootmode="open"><!----> <!--?lit$846942102$--> <div class="cell-status">
        <button title="Placer le curseur sur la dernière cellule exécutée

23:39 (il y a 9 heures)
exécuté en 0.262 s"><!--?lit$846942102$--><md-icon class="success" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$--><svg viewBox="0 0 24 24"><!--?lit$846942102$--><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"></path></svg></md-icon>&nbsp; <!--?lit$846942102$-->0&nbsp;s</button>
        <button title="Afficher l&#39;historique du code exécuté

23:39 (il y a 9 heures)
exécuté en 0.262 s"><!--?lit$846942102$-->terminée à 23:39</button>
      </div>
      <md-icon-button class="visible-on-closed" title="Environnement d&#39;exécution déconnecté" disabled="" value="" data-aria-label="Environnement d&#39;exécution déconnecté"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Environnement d&#39;exécution déconnecté" disabled="">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon filled="" class="visible-on-closed" status="icon-error" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$846942102$-->fiber_manual_record</md-icon>
      </md-icon-button>
      <!--?lit$846942102$-->
      <md-icon-button title="Fermer" data-aria-label="Fermer" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Fermer">
        <!--?lit$846942102$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$846942102$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$846942102$--><span class="icon"><slot></slot></span>
        <!--?lit$846942102$-->
        <!--?lit$846942102$--><span class="touch"></span>
        <!--?lit$846942102$-->
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button></template></colab-status-bar></div><div class="goog-menu colab-styled-scroller" id="file-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 63.9931px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Trouver dans Google&nbsp;Drive<!--?lit$846942102$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Ouvrir en mode brouillon<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Nouveau notebook dans Drive<!--?lit$846942102$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Ouvrir le notebook<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+O</span></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Importer le notebook<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Renommer<!--?lit$846942102$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Déplacer<!--?lit$846942102$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Placer dans la corbeille<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Enregistrer une copie dans Drive<!--?lit$846942102$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Enregistrer une copie en tant que fichier Gist GitHub<!--?lit$846942102$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Enregistrer une copie dans GitHub<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Enregistrer<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+S</span></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Enregistrer et épingler cette version<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M S</span></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Historique des versions<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$846942102$-->Télécharger
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Imprimer<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+P</span></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$846942102$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Télécharger le fichier .ipynb<!--?lit$846942102$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Télécharger le code .py<!--?lit$846942102$--></div></div></div><div class="goog-menu colab-styled-scroller" id="edit-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 119.931px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Annuler la suppression de cellule<span class="goog-menuitem-accel">Ctrl+M Z</span></div></div><div command="redo" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":r" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">Répéter<span class="goog-menuitem-accel">Ctrl+Shift+Y</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Sélectionner toutes les cellules<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Shift+A</span></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Couper la cellule ou la sélection<!--?lit$846942102$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Copier la cellule ou la sélection<!--?lit$846942102$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Coller<!--?lit$846942102$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Supprimer les cellules sélectionnées<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M D</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Rechercher et remplacer<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+H</span></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Rechercher l'occurrence suivante<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+G</span></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Rechercher l'occurrence précédente<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Shift+G</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Paramètres du notebook<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Supprimer tous les résultats<!--?lit$846942102$--></div></div></div><div class="goog-menu colab-styled-scroller" id="view-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 185.538px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----> </div><!--?lit$846942102$-->Sommaire<!--?lit$846942102$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Informations sur le notebook<!--?lit$846942102$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Historique d'exécution<!--?lit$846942102$--></div></div><div command="toggle-comments-visibility" class="goog-menuitem goog-option goog-option-selected" role="menuitemcheckbox" aria-checked="true" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$846942102$-->Barre latérale des commentaires<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1b" style="user-select: none;"></div><div command="collapse-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1c" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Réduire les rubriques<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+]</span></div></div><div command="expand-sections" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1d" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Développer les rubriques<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+[</span></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1e" style="user-select: none; display: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Enregistrer la mise en page à sections réduites<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1f" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Afficher/Masquer le code<!--?lit$846942102$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Afficher/Masquer le résultat<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M O</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1i" style="user-select: none;"></div><div command="focus-next-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1j" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Placer le curseur sur l'onglet suivant<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Shift+]</span></div></div><div command="focus-previous-tab" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1k" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Placer le curseur sur l'onglet précédent<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Shift+[</span></div></div><div command="move-tab-to-next" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1l" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Déplacer l'onglet vers le volet suivant<!--?lit$846942102$--></div></div><div command="move-tab-to-prev" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":1m" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Déplacer l'onglet vers le volet précédent<!--?lit$846942102$--></div></div></div><div class="goog-menu colab-styled-scroller" id="insert-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 258.75px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Cellule de code<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M B</span></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Cellule de texte<!--?lit$846942102$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Cellule d'en-tête de section<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1r" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Cellule de code bloc-notes<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Alt+N</span></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Extraits de code<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Alt+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1u" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Ajouter un champ de formulaire<!--?lit$846942102$--></div></div></div><div class="goog-menu colab-styled-scroller" id="runtime-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 315.885px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Tout exécuter<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+F9</span></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Exécuter avant<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+F8</span></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":1z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Exécuter la cellule sélectionnée<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Enter</span></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Exécuter le code sélectionné<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Shift+Enter</span></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":21" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Exécuter la cellule et celles du dessous<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+F10</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":22" style="user-select: none;"></div><div command="interrupt" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":23" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Interrompre l'exécution<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M I</span></div></div><div command="restart" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":24" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Redémarrer la session<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M .</span></div></div><div command="restart-and-run-all" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":25" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Redémarrer la session et tout exécuter<!--?lit$846942102$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Déconnecter et supprimer l'environnement d'exécution<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Modifier le type d'exécution<!--?lit$846942102$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":29" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Gérer les sessions<!--?lit$846942102$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Afficher les ressources<!--?lit$846942102$--></div></div><div command="view-runtime-logs" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":2c" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Afficher les journaux d'exécution<!--?lit$846942102$--></div></div></div><div class="goog-menu colab-styled-scroller" id="tools-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 390.99px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="show-command-palette" class="goog-menuitem" role="menuitem" id=":2e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Palette de commandes<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Shift+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2f" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Paramètres<!--?lit$846942102$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Raccourcis clavier<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+M H</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2i" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Diff. entre notebooks<!--?lit$846942102$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$846942102$-->(s'ouvre dans un nouvel onglet)</span></div></div></div><div class="goog-menu colab-styled-scroller" id="help-menu" role="menu" aria-haspopup="true" style="user-select: none; max-height: 655.017px; visibility: visible; left: 441.128px; top: 61.9826px; display: none;"><!--?lit$846942102$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Questions fréquentes<!--?lit$846942102$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Consulter les notes de version<!--?lit$846942102$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Rechercher des extraits de code<!--?lit$846942102$--><span class="goog-menuitem-accel">Ctrl+Alt+P</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2o" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Signaler un bug<!--?lit$846942102$--></div></div><div command="report-abuse" class="goog-menuitem goog-menuitem-disabled" role="menuitem" id=":2q" aria-disabled="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Signaler un abus dans Drive<!--?lit$846942102$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Donner votre avis<!--?lit$846942102$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Afficher les conditions d'utilisation<!--?lit$846942102$--></div></div><div command="view-in-english" class=" goog-menuitem " role="menuitem" id=":2t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$846942102$-->Afficher en anglais<!--?lit$846942102$--></div></div></div><dialog class="doc-comments-area" aria-label="Commentaires"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$846942102$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$846942102$--><button id="button" class="button">
      <!--?lit$846942102$-->
      <span class="touch"></span>
      <!--?lit$846942102$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$846942102$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$846942102$-->Ajouter un commentaire
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true" style="visibility: visible;">f.show()</div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy3a4604a5ffa9d97303168bdfa6cfe27789def84b0.441605268" name="apiproxy3a4604a5ffa9d97303168bdfa6cfe27789def84b0.441605268" src="./Analyse de données_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div>Impossible d'établir une connexion avec le service reCAPTCHA. Veuillez vérifier votre connexion Internet, puis actualiser la page pour afficher une image reCAPTCHA.</div></div><iframe src="./Analyse de données_files/bscframe.html" style="display: none;"></iframe><iframe frameborder="0" src="./Analyse de données_files/saved_resource(8).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":dx" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":dx" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":dx.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":dy" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":dy" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":dy.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare.html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><iframe frameborder="0" src="./Analyse de données_files/saved_resource(9).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":dz" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":dz" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":dz.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":e0" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e0" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":e0.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare(1).html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><iframe frameborder="0" src="./Analyse de données_files/saved_resource(10).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":e1" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e1" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":e1.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":e2" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e2" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":e2.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare(2).html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><iframe frameborder="0" src="./Analyse de données_files/saved_resource(11).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":e3" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e3" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":e3.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":e4" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e4" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":e4.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare(3).html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><iframe frameborder="0" src="./Analyse de données_files/saved_resource(12).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":e5" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e5" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":e5.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":e6" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":e6" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":e6.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare(4).html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><iframe frameborder="0" src="./Analyse de données_files/saved_resource(13).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":j2" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":j2" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":j2.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":j3" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":j3" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":j3.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare(5).html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><iframe frameborder="0" src="./Analyse de données_files/saved_resource(14).html" class="modal-dialog-bg" style="border: 0px; vertical-align: bottom; opacity: 0; width: 1509px; height: 740px; display: none;"></iframe><div class="modal-dialog-bg" style="opacity: 0.5; width: 1509px; height: 740px; display: none;"></div><div class="modal-dialog share-client-loading-dialog" tabindex="0" role="dialog" aria-labelledby=":ka" style="left: 518px; top: 286.5px; display: none;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":ka" role="heading">Chargement…</span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer"></span></div><div class="modal-dialog-content" id=":ka.contentEl"><div class="share-client-loading-contents"><div class="share-client-spinner"> </div></div></div><div class="modal-dialog-buttons" style="display: none;"></div></div><span tabindex="0" style="position: absolute; left: 518px; top: 286.5px; display: none;"></span><div class="modal-dialog share-client-dialog full-screen-share-client-dialog team-drive-share-client-dialog share-client-offscreen" tabindex="-1" role="dialog" aria-labelledby=":kb" guidedhelpid="drive_share_dialog" aria-hidden="true" style="left: 0px; top: 0px;"><div class="modal-dialog-title modal-dialog-title-draggable"><span class="modal-dialog-title-text" id=":kb" role="heading"></span><span class="modal-dialog-title-close" role="button" tabindex="0" aria-label="Fermer" aria-hidden="true" style="display: none;"></span></div><div class="modal-dialog-content" id=":kb.contentEl"><iframe frameborder="0" src="./Analyse de données_files/driveshare(6).html" class="share-client-content-iframe" title="Contenu" tabindex="-1"></iframe></div><div class="modal-dialog-buttons" style="display: none;"></div><div class="share-client-debug"></div></div><span tabindex="-1" style="position: absolute; left: 0px; top: 0px;"></span><colab-callout dismisstext="" tooltipstyling="" aria-label="Renommer le notebook" opened="" role="tooltip" verticaldirection="below" horizontaldirection="right" style="visibility: visible; top: 36.9883px; left: 90.9375px;"><template shadowrootmode="open"><!----> <div id="content"><slot name="content"></slot></div>
      <!--?lit$846942102$--><!--?--></template>
      <!--?lit$846942102$--><div slot="content"><!----><!--?lit$846942102$--><!----><div><!--?lit$846942102$-->Renommer le notebook</div><!----><!--?--></div>
    </colab-callout></body></html>