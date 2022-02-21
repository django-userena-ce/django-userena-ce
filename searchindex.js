Search.setIndex({docnames:["api/backends","api/decorators","api/forms","api/index","api/managers","api/middleware","api/models","api/utils","api/views","commands","contrib/umessages/api/index","contrib/umessages/api/managers","contrib/umessages/api/views","contrib/umessages/index","faq","index","installation","settings","signals"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,sphinx:56},filenames:["api/backends.rst","api/decorators.rst","api/forms.rst","api/index.rst","api/managers.rst","api/middleware.rst","api/models.rst","api/utils.rst","api/views.rst","commands.rst","contrib/umessages/api/index.rst","contrib/umessages/api/managers.rst","contrib/umessages/api/views.rst","contrib/umessages/index.rst","faq.rst","index.rst","installation.rst","settings.rst","signals.rst"],objects:{"userena.backends":[[0,1,1,"","UserenaAuthenticationBackend"]],"userena.backends.UserenaAuthenticationBackend":[[0,2,1,"","authenticate"]],"userena.contrib.umessages":[[11,0,0,"-","managers"],[12,0,0,"-","views"]],"userena.contrib.umessages.managers":[[11,1,1,"","MessageManager"]],"userena.contrib.umessages.managers.MessageManager":[[11,2,1,"","get_conversation_between"],[11,2,1,"","send_message"]],"userena.contrib.umessages.views":[[12,3,1,"","MessageDetailListView"],[12,3,1,"","MessageListView"],[12,3,1,"","message_compose"],[12,3,1,"","message_remove"]],"userena.decorators":[[1,3,1,"","secure_required"]],"userena.forms":[[2,1,1,"","AuthenticationForm"],[2,1,1,"","ChangeEmailForm"],[2,1,1,"","EditProfileForm"],[2,1,1,"","SignupForm"],[2,1,1,"","SignupFormOnlyEmail"],[2,1,1,"","SignupFormTos"]],"userena.forms.AuthenticationForm":[[2,2,1,"","clean"],[2,4,1,"","media"]],"userena.forms.ChangeEmailForm":[[2,2,1,"","clean_email"],[2,4,1,"","media"],[2,2,1,"","save"]],"userena.forms.EditProfileForm":[[2,4,1,"","media"],[2,2,1,"","save"]],"userena.forms.SignupForm":[[2,2,1,"","clean"],[2,2,1,"","clean_email"],[2,2,1,"","clean_username"],[2,4,1,"","media"],[2,2,1,"","save"]],"userena.forms.SignupFormOnlyEmail":[[2,4,1,"","media"],[2,2,1,"","save"]],"userena.forms.SignupFormTos":[[2,4,1,"","media"]],"userena.managers":[[4,1,1,"","UserenaBaseProfileManager"],[4,1,1,"","UserenaManager"]],"userena.managers.UserenaBaseProfileManager":[[4,2,1,"","get_visible_profiles"]],"userena.managers.UserenaManager":[[4,2,1,"","activate_user"],[4,2,1,"","check_expired_activation"],[4,2,1,"","check_permissions"],[4,2,1,"","confirm_email"],[4,2,1,"","create_user"],[4,2,1,"","create_userena_profile"],[4,2,1,"","delete_expired_users"],[4,2,1,"","reissue_activation"]],"userena.middleware":[[5,1,1,"","UserenaLocaleMiddleware"]],"userena.models":[[6,1,1,"","UserenaBaseProfile"],[6,1,1,"","UserenaLanguageBaseProfile"],[6,1,1,"","UserenaSignup"],[6,3,1,"","upload_to_mugshot"]],"userena.models.UserenaBaseProfile":[[6,1,1,"","Meta"],[6,2,1,"","can_view_profile"],[6,2,1,"","get_full_name_or_username"],[6,2,1,"","get_mugshot_url"]],"userena.models.UserenaLanguageBaseProfile":[[6,1,1,"","Meta"]],"userena.models.UserenaSignup":[[6,5,1,"","DoesNotExist"],[6,5,1,"","MultipleObjectsReturned"],[6,2,1,"","activation_key_expired"],[6,2,1,"","change_email"],[6,2,1,"","send_activation_email"],[6,2,1,"","send_confirmation_email"]],"userena.utils":[[7,3,1,"","generate_nonce"],[7,3,1,"","get_gravatar"],[7,3,1,"","get_profile_model"],[7,3,1,"","signin_redirect"]],"userena.views":[[8,3,1,"","activate"],[8,3,1,"","direct_to_user_template"],[8,3,1,"","email_change"],[8,3,1,"","email_confirm"],[8,3,1,"","password_change"],[8,3,1,"","profile_detail"],[8,3,1,"","profile_edit"],[8,3,1,"","profile_list"],[8,3,1,"","signin"],[8,3,1,"","signup"]],userena:[[0,0,0,"-","backends"],[1,0,0,"-","decorators"],[2,0,0,"-","forms"],[4,0,0,"-","managers"],[5,0,0,"-","middleware"],[6,0,0,"-","models"],[7,0,0,"-","utils"],[8,0,0,"-","views"]]},objnames:{"0":["py","module","Python module"],"1":["py","class","Python class"],"2":["py","method","Python method"],"3":["py","function","Python function"],"4":["py","property","Python property"],"5":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:class","2":"py:method","3":"py:function","4":"py:property","5":"py:exception"},terms:{"0":[15,16],"1":[0,8,16],"11":16,"2":[0,16,17],"3":16,"30":[14,17],"4":16,"40":[7,8],"404":[7,8,17],"5":16,"50":8,"587":16,"6":16,"7":[15,16,17],"8":16,"80":[7,17],"9":16,"abstract":[6,16],"boolean":[0,4,6,8,12,17],"case":[4,6,14],"char":7,"class":[0,2,4,5,6,7,8,11,12,14,16,18],"default":[4,6,7,8,12,14,15,16,17],"do":[7,15,16,17],"final":14,"function":[4,6,8,12,16],"import":[14,16],"int":17,"long":[7,8],"new":[2,4,6,8,12,14,17],"public":8,"return":[0,1,2,4,5,6,7,8,11,12,14,17],"super":14,"switch":[1,5,15],"true":[0,2,4,6,8,12,16,17],"try":[0,8,17],A:[0,2,4,6,7,8,11,12,13,15,17,18],And:[2,8],As:[16,17],By:[6,16],For:[4,6,8,9,13,14,15,16],If:[1,2,4,6,7,8,12,14,15,16,17],In:[16,17],Is:17,It:[2,5,8,16,17],Not:[7,17],One:[6,14],Or:16,That:14,The:[0,1,2,4,6,7,8,11,12,15,17,18],Then:16,There:17,To:[14,16],Will:8,With:17,_:[14,16],__init__:14,abil:16,abl:[0,6,8],about:8,abov:[14,16],access:[1,8],account:[2,7,8,14,15,16,17,18],across:8,action:[8,18],activ:[0,3,4,6,7,15,17,18],activate_fail:8,activate_form:8,activate_retri:8,activate_us:4,activation_complet:[4,15],activation_form:8,activation_kei:[4,6,8,17],activation_key_cr:6,activation_key_expir:6,activationform:8,ad:[8,13,14,16],adapt:2,add:[2,13,15,16,17],add_myprofil:6,add_profil:6,address:[2,4,6,7,8,9,17,18],admin:[6,14,16,17],administr:8,after:[2,4,6,7,8,9,12,16,17],all:[2,4,6,7,8,14,15,16,17,18],allow:[4,8,17],almost:8,alphanumer:2,alreadi:[2,9,15,16],already_activ:17,also:[1,2,4,6,8,12,13,14,16,17],alter:[8,16],alwai:[0,2,6,8,14,17],amount:[6,8,17],an:[1,2,4,6,7,8,9,12,15,16,17,18],ani:[7,12,17],anonym:17,anonymous_user_id:16,anonymous_user_nam:16,anonymousus:16,anoth:[2,6],api:[0,1,2,4,5,6,13,15],append:17,appli:[1,2,4],applic:[8,13,15,16,18],ar:[2,4,6,8,9,11,12,14,15,16,17,18],arg:[2,4,6,11,14],argument:[0,7,8,17,18],ask:2,associ:[4,7,17],attach:14,auth:[8,16],auth_form:8,auth_profile_modul:[7,16],authent:[0,8],authentication_backend:16,authenticationform:[3,8],auto_id:2,automag:16,automat:[6,17],avail:[4,15,16],awai:17,back:[2,7],backend:[3,15],background:[7,17],base:[2,6,7,16,17],basi:15,basic:[6,16],becaus:[0,1,2,6,8,14,15],becom:6,befor:[2,6,7,16,17],begin:16,being:[8,17],best:17,between:[11,12,15],beyond:6,bit:14,blob:14,bodi:11,bread:15,brows:6,bug:15,button:2,call:[2,6,8,14],can:[2,5,6,7,8,12,15,16,17,18],can_view_profil:6,cannot:[16,17],care:[14,15],cartoon:[7,17],cascad:16,caus:16,cd:16,ce:[14,15],chang:[6,8,16,17,18],change_email:[2,6],change_profil:[6,14],changeemailform:[3,8],chapter:16,charact:8,charfield:[14,16],check:[0,1,2,4,6,8,14,15],check_expired_activ:4,check_password:0,check_permiss:[4,9,14,16],choic:6,choos:[16,17],chosen:16,clean:[2,15],clean_email:2,clean_expir:9,clean_usernam:2,cleaned_data:14,cleanexpir:[9,17],click:[4,6,15],clone:16,close:[4,6,17],code:[4,15,16],color:[7,17],com:[14,16],combin:[0,2,6,8],come:[9,17],command:[14,15,16,17],commit:2,complet:8,compos:12,compose_form:12,composeform:12,configur:16,confirm:[4,6,8],confirm_email:[4,6,8],confirmation_complet:[4,15],confirmation_kei:[4,8],connect:16,consult:16,contact:[12,15],contain:[0,4,6,7,8,11,12,16,17,18],context:[8,12],contrib:[8,11,12,13,16],conveni:[16,17],convers:[11,12,15],cooki:5,copi:16,core:[8,16],correct:[8,9],correctli:[4,9],could:[4,8,14,16],counterpart:17,cover:15,creat:[2,4,6,14,15,16,17],create_us:[4,14],create_userena_profil:4,cronjob:9,cryptograph:[7,8],current:[4,7,8,9,17],custom:[0,2,6,14,16,17,18],custom_profil:14,dai:[6,17],data:2,date:17,date_join:17,date_now:17,decid:[14,16],declar:16,decor:[3,15,17],def:14,defin:[0,4,6,7,8,16,17],delet:[4,9,12,15,17],delete_expired_us:4,demis:17,demo:14,demonstr:14,deni:[8,17],depend:[5,6],design:17,desir:16,detail:8,dictionari:[8,12],differ:[7,17],direct:[8,16],direct_to_templ:8,direct_to_user_templ:3,directli:16,directori:[6,16],disabl:[1,8,17],displai:[7,8,15,17],divid:6,django:[0,2,4,5,6,7,8,14,15,18],doc:[14,16],document:[15,16],doe:[7,15,16,17],doesn:[1,2,5,18],doesnotexist:[4,6,14],domain:16,don:[4,6,12,14,15],done:[14,15],download:16,dummi:16,e:[0,2,4,8,9,16],each:[14,16],easy_thumbnail:16,edit:[8,15],edit_profile_form:8,editprofileform:[3,8],egg:16,either:[15,17],ek:16,element:11,email:[0,2,4,6,7,8,14,15,17,18],email_backend:16,email_chang:3,email_confirm:3,email_confirm_fail:8,email_confirmation_kei:6,email_form:8,email_host:16,email_host_password:16,email_host_us:16,email_port:16,email_use_tl:16,emailbackend:16,emerg:9,empti:8,empty_permit:2,en:14,enabl:[1,2,8,17],end:[2,14,16],enter:2,entir:8,environ:16,error:[2,14],error_class:2,errorlist:2,especi:17,etc:[6,7,17],even:17,everi:14,everyon:[4,6],ex:[6,8,16,17],exampl:[9,13,14,16,17],except:[4,6,15],exist:[9,15],expect:14,experi:17,expir:[4,6,8,15,17],explicitli:16,extend:[6,14,17],extra:[4,6,8,12,15,16,17],extra_context:[8,12],extra_field:14,extraprofil:14,f:[15,17],face:[7,17],facil:16,fail:[7,8],fail_template_nam:8,fall:[2,7],fallback:17,fals:[2,4,6,12,14,17],faq:17,favourit:16,favourite_snack:16,featur:[7,17],few:[17,18],field:[2,6,7,8,15,16,17],field_ord:2,file:[2,7,15,16,17,18],filenam:6,fire:18,first:[0,7,8,14,16,17],first_nam:14,fit:15,fix:14,follow:[7,8,12,14,15,16,17],force_insert:2,force_upd:2,forget:14,fork:[15,16],form:[0,3,7,8,12,15,17],format:[8,16],found:[2,4,7,8,15,17],four:6,framework:17,from:[0,1,8,11,14,15,17],full:6,fulli:16,further:16,g:16,gener:[2,7,8,17],generate_nonc:3,geometr:[7,17],get:[6,7,8,9,12,15,16,17,18],get_conversation_between:11,get_full_name_or_usernam:6,get_gravatar:3,get_mugshot_url:6,get_profile_model:3,get_respons:5,get_visible_profil:4,gettext:[16,17],gettext_lazi:14,github:[14,15,16],gmail:[15,16],go:[6,7],goe:14,gravatar:[6,7,15,17],great:13,group:6,guardedmodeladmin:17,guardian:[15,16],ha:[4,6,7,8,12,15,16,17,18],hackeri:14,handl:8,happen:17,hard:15,hash:[0,6,7,17],have:[6,8,12,13,15,16,17,18],haven:[9,17],here:[2,14],hi:[8,17],higher:16,histori:15,how:[6,15,17],html:[8,12,14,17],http:[1,7,14,15,16,17],human:17,i:[15,17],id:[12,16,17],id_:2,identicon:[7,17],identif:[0,2,17],imag:[6,7,17],imit:12,implement:[6,9,15],improv:15,inbox:12,includ:[13,16],incorrect:14,index:15,inform:[6,12,16],inherit:16,initi:2,instal:[14,15],installed_app:[13,16],instanc:[2,4,6,8],instead:[7,8,14,17],instruct:[14,16],integ:[8,17],integr:16,invalid:[2,4,8],iphon:[12,13,15],is_act:8,is_pagin:8,is_staff:4,is_valid:8,isol:16,issu:[15,16,17],its:16,itself:[8,16],join:6,just:[4,6,7,16,17],keep:[0,2,4,8],kei:[2,4,6,8,12,16,17],ket:4,keyword:8,know:6,kw:[2,14],kwarg:[2,4,6,8,11,12],l65:14,label:14,label_suffix:2,languag:[5,6,16,17],last:[12,14],last_nam:14,later:[2,8,13],latest:14,left:8,let:[4,6,14,16],like:[6,13,15,16],link:[4,8,15],list:[2,4,8,11,12,17],live:16,ll:16,ln:16,load:[7,17],locat:18,log:[8,16,17],logic:[8,14],login:[0,8,17],login_redirect_url:7,login_requir:17,login_url:16,logout:17,logout_url:16,look:[5,6,7,16],made:[6,8,17],mai:16,mail:[0,2,4,8,9,16],make:[6,16],makemigr:16,man:[7,17],manag:[3,9,10,13,14,15,16],manual:[2,15],master:14,match:[2,15],max_length:[14,16],md:15,me:17,mean:[14,16,18],media:2,media_path:17,messag:[8,11,12,13,15,17],message_compos:10,message_form:12,message_pk:12,message_remov:10,messagedetaillistview:10,messagelistview:10,messagemanag:10,meta:6,method:[0,2,6,8,14],middlewar:[3,15,16],middleware_class:16,migrat:15,minor:8,mirror:8,miss:14,mm:[7,17],model:[2,3,4,7,11,14,15,16,17],modelbackend:16,modifi:16,monster:[7,17],monsterid:[7,17],month:17,more:[6,14],move_to_end:14,mugshot:[6,15,16,17],multipart:17,multipl:[12,15],multipleobjectsreturn:6,must:[0,1,8,16,17],my:14,my_profil:[14,16],mynewus:14,myprofil:[6,16],mysteri:[7,17],name:[6,8,12,14,16,17],neccesari:12,necessari:[6,16],need:[2,6,8,9,13,14,15,16],new_ord:14,new_us:14,newli:[2,4,6,14,17],next:[7,8,12,16],nobodi:6,non_field_error:2,nonc:[4,7,8],none:[0,2,4,5,6,7,8,12,17],normal:[7,17],note:[2,14,16,17,18],notif:17,notifi:17,now:[4,16],object:[2,6,7,8,14,15,16,17],objectpermissionbackend:16,off:17,offer:16,often:17,old:[6,15,17,18],old_email:18,on_delet:16,onc:17,one:[2,6,7,12,16,17],onetoonefield:16,onli:[0,4,6,9,12,15,16,17],onto:8,open:[0,6,16,17],option:[0,6,7,15,16,17],org:14,other:[6,8,17],otherwis:2,our:[8,14],out:[2,6,9,17],outlin:[7,17],outsid:14,overrid:[5,14,15,17],overridden:17,own:[4,14,16,17,18],owner:[6,17],packag:16,page:[0,7,8,12,15,16],page_obj:8,pagin:8,paginate_bi:8,paramet:[0,4,6,7,8,11,12],parent:[2,14],part:17,pass:8,pass_form:8,password:[0,2,4,8,17,18],password_chang:3,password_complet:15,password_form:8,passwordchangeform:8,path:17,pattern:[7,17],pepper:15,per:[8,15,17],perman:1,permiss:[4,6,8,15,17],permisson:17,person:[7,17],pixel:[7,17],place:[14,16],plain:17,plug:15,point:[7,17],posit:0,possibl:[8,16],post:12,prefer:[7,16,17],prefix:[2,16],present:[4,16],prevent:17,previou:4,print:16,privaci:[6,15,16,17],privat:15,probabl:16,proce:8,profil:[4,5,6,7,8,15,17],profile_detail:[3,17],profile_edit:3,profile_form:8,profile_list:[3,17],profilemodel:15,project:[1,9,15,16,17],prompt:16,properti:2,protocol:[15,17],provid:[16,18],put:[14,16],py:[9,14,16,17,18],python:15,python_path:16,pythonpath:16,q:15,queri:15,r:[13,14,16],rais:[2,4],random:2,readabl:17,reason:6,receiv:[12,14],recipi:12,recipient_filt:12,recommend:16,redirect:[1,7,8,12,17],redirect_field_nam:8,redirect_signin_funct:8,refer:[0,1,2,4,5,6,13,15],reflect:16,regist:[2,4,6,15,17],regit:17,reissu:17,reissue_activ:4,related_nam:16,relev:17,rememb:[8,17],remov:[12,16],render:[2,8,17],replac:[8,16],repositori:[15,16],repres:[4,8,17],request:[0,2,6,8,12,17],requested_redirect:7,requir:[0,2,4,7,8,14,15,17],reregist:17,reregit:17,reset:4,respect:17,respons:[7,17],rest:8,result:8,retry_template_nam:8,revers:8,right:6,root:16,run:[8,9,14,17],s:[2,4,6,7,8,9,12,13,14,15,17,18],same:[1,17],save:[2,6,8,14,17],save_m2m:2,screen:16,search:[9,15],secret:[0,4],section:14,secur:[1,15,17],secure_requir:3,see:[14,15,16,17],select:8,self:[2,4,14],send:[2,4,6,11,12,16,17],send_activation_email:6,send_confirmation_email:6,send_email:4,send_messag:11,send_verification_email:6,sender:11,sensit:17,sent:[4,15],seper:12,servic:[2,17],set:[2,4,5,6,7,8,9,13,14,15],setup:16,shell:16,should:[0,1,4,6,7,8,12,14,16,17],shouldn:9,show:[6,8,12],shown:[8,16],side:[7,17],sign:[0,2,6,7,8,12,17,18],signal:[4,15],signin:[3,15,16,17],signin_form:8,signin_redirect:[3,8],signout:[16,17],signup:[2,3,14,15,16,17],signup_complet:[8,15],signup_form:[8,14,17],signupextraprofileform:14,signupform:[3,8,14],signupformextra:14,signupformonlyemail:3,signupformto:3,silhouet:[7,17],simpl:[4,7,8,17],singl:2,site:[15,16,18],site_id:[14,16],situat:9,size:[7,17],skip:[4,16],sm:12,smtp:16,snack:16,so:[5,6,8,14,16,17],some:[9,16],someth:14,sometim:[14,16],sort:15,special:6,specif:[7,8,16],specifi:[7,8,17],squar:7,src:16,stadium:8,stand:17,standard:[7,14],startapp:16,still:[4,5,6,9,15,17],store:6,string:[0,4,6,7,8,11,12,17,18],style:[7,17],subject:15,succeed:8,succesfulli:18,success:[4,7,8,17],success_url:[8,12,17],successful:12,successfulli:8,suitabl:16,superadmin:6,suppli:[0,2,4,6,7,8,12,13,14,15,16],support:[1,15],symlink:16,syncdb:13,system:[13,15],t:[1,2,4,5,6,9,12,14,15,17,18],tailor:16,take:[14,15],tell:[14,16],templat:[8,12,14,15,17],template_nam:[8,12],temporari:6,temporary_email:6,term:2,termin:16,test:16,text:17,than:[1,2,6,14],thei:[6,17],them:[2,9,12,15,16],thi:[0,1,2,4,6,7,8,9,12,14,15,16,17,18],thing:14,those:[14,15],thousand:14,three:[16,17],through:[0,1,4,6,8],thu:[2,14,17],time:2,timefram:4,titl:16,todo:8,top:[12,14,16],translat:[14,16],tupl:17,turn:17,tweak:17,twice:2,two:[2,6,9,11,12,16],type:[14,16],u:14,udat:15,um_from_us:11,um_to_us:11,um_to_user_list:11,umesagg:13,umessag:[11,12],under:[6,16],undo:12,uninstal:16,uniqu:[2,6,16],unregist:[14,17],unremov:12,up:[2,16,17,18],updat:16,upload:[6,15,17],upload_to_mugshot:3,uri:[6,7,8,12,14,17],url:[1,8,12,13,14,16,17],urlconf:[13,16],urlpattern:16,us:[0,2,4,6,7,8,12,14,15,16,17,18],use_required_attribut:2,user:[0,2,4,5,6,7,8,9,11,12,13,15,16,17,18],user_profil:14,userena:[0,1,2,4,5,6,7,8,9,11,12,13,14,18],userena_activ:6,userena_activation_dai:[6,9],userena_detail:8,userena_disable_profile_list:8,userena_email_complet:8,userena_forbidden_usernam:2,userena_mugshot_default:6,userena_mugshot_gravatar:6,userena_mugshot_path:6,userena_password_complet:8,userena_profile_detail:8,userena_remember_dai:8,userena_signin_redirect_url:16,userena_signup_complet:8,userena_umessages_detail:12,userena_umessages_list:12,userena_use_http:1,userena_without_usernam:[2,6],userenaauthenticationbackend:[0,16],userenabaseprofil:[3,16],userenabaseprofilemanag:3,userenalanguagebaseprofil:[3,16],userenalocalemiddlewar:[3,6,16],userenamanag:3,userenaprofil:4,userenasignup:[3,4,8,14],userenaus:6,usernam:[0,2,4,6,8,12,16,17],util:[2,3,14,15,16],v2:16,valid:[2,4,6],valu:[2,6,7,8,12,14,17],vari:[7,17],variabl:[8,12,16,17],verbose_nam:16,verif:[2,4,6,16],verifi:[2,4,6,8,9],version:[1,15,17],via:17,view:[1,3,4,6,7,10,13,14,15,16,17],view_func:1,viewed_us:8,virtualenv:16,visibl:4,wa:[4,8,12,16],wai:[6,14,16],want:[4,6,8,12,14,16,17,18],warn:17,wavatar:[7,17],we:[6,8,15,16],web:8,websit:[6,17],what:[6,7],when:[0,2,4,6,8,9,17,18],whenev:14,where:[2,8,17],whether:[8,17],which:[2,6,7,8,11,12,16,17,18],who:[7,8],whom:[6,11,12],whose:[4,8],widget:2,within:17,word:14,work:[15,16],would:[6,17],wrapper:[4,8],wrong:4,ye:14,you:[4,8,13,14,15,16,17,18],your:[4,6,8,13,14,15,16,17,18],your_profile_admin:14,your_profile_model:14,your_python_path:16,yourgmailaccount:16,yourgmailpassword:16,yourself:17,yoursit:16},titles:["Backends","Decorators","Forms","API Reference","Managers","Middleware","Models","Utils","Views","Commands.","API Reference","Managers","Views","uMessages","F.A.Q","Userena Introduction","Installation.","Settings","Signals"],titleterms:{"do":14,"new":16,A:14,The:16,activ:8,activation_complet:18,add:14,alreadi:14,api:[3,10],app:16,auth_profile_modul:17,authenticationform:2,automat:16,backend:[0,16],bread:16,can:14,ce:16,chang:15,changeemailform:2,check:[9,16],clean:9,command:9,confirmation_complet:18,content:15,contrib:15,decor:1,develop:16,direct_to_user_templ:8,django:[16,17],doe:14,easy_instal:16,editprofileform:2,email:16,email_chang:8,email_confirm:8,except:14,exist:14,expir:9,extra:14,f:14,field:14,form:[2,14],from:16,generate_nonc:7,get:14,get_gravatar:7,get_profile_model:7,git:16,have:14,help:15,how:14,i:14,indic:15,instal:[13,16],introduct:15,login_redirect_url:17,login_url:17,logout_url:17,manag:[4,11],manual:[14,16],match:14,message_compos:12,message_remov:12,messagedetaillistview:12,messagelistview:12,messagemanag:11,middlewar:5,migrat:16,model:6,multipl:14,old:16,out:15,password_chang:8,password_complet:18,pepper:16,per:14,permiss:[9,14,16],pip:16,profil:[14,16],profile_detail:8,profile_edit:8,profile_list:8,profilemodel:14,python:16,q:14,queri:14,refer:[3,10],regist:14,releas:15,requir:16,run:16,s:16,secure_requir:1,set:[16,17],signal:18,signin:8,signin_redirect:7,signup:8,signup_complet:18,signupform:2,signupformonlyemail:2,signupformto:2,site:14,start:16,still:14,support:16,tabl:15,umessag:[13,15],upload_to_mugshot:6,uri:16,user:14,userena:[15,16,17],userena_activ:17,userena_activation_dai:17,userena_activation_notifi:17,userena_activation_notify_dai:17,userena_activation_requir:17,userena_activation_retri:17,userena_default_privaci:17,userena_disable_profile_list:17,userena_disable_signup:17,userena_forbidden_usernam:17,userena_hide_email:17,userena_html_email:17,userena_language_field:17,userena_mugshot_default:17,userena_mugshot_gravatar:17,userena_mugshot_gravatar_secur:17,userena_mugshot_path:17,userena_mugshot_s:17,userena_profile_detail_templ:17,userena_profile_list_templ:17,userena_register_profil:17,userena_register_us:17,userena_remember_me_dai:17,userena_signin_after_signup:17,userena_signin_redirect_url:17,userena_use_http:17,userena_use_messag:17,userena_use_plain_templ:17,userena_without_usernam:17,userenabaseprofil:6,userenabaseprofilemanag:4,userenalanguagebaseprofil:6,userenalocalemiddlewar:5,userenamanag:4,userenasignup:6,util:7,version:16,view:[8,12],why:15}})