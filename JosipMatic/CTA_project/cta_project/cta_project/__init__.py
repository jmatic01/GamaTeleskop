from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
import pymongo
from pymongo import MongoClient
from pyramid.response import Response
from cta_project.resources import Root
import csv
def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    config.add_view('cta_project.views.my_view',
                    context='cta_project:resources.Root',
                    renderer='cta_project:templates/mytemplate.pt')
    config.add_static_view('static', 'cta_project:static')
    config.include('pyramid_chameleon')
    config.add_route('csv2' , '/csv2')
    config.add_route('wea_ws', '/wea_ws')
    config.add_view('cta_project.views.csvview', route_name = 'csv2')
    config.add_view('cta_project.views.wea_ws', route_name = 'wea_ws')
    config.add_route('wea_hum', '/wea_hum')
    config.add_view('cta_project.views.wea_hum', route_name = 'wea_hum')
    config.add_route('wea_gust', '/wea_gust')
    config.add_view('cta_project.views.wea_gust', route_name = 'wea_gust')
	
    config.add_route('wea_see', '/wea_see')
    config.add_view('cta_project.views.wea_see', route_name = 'wea_see')
	
    config.add_route('wea_dust', '/wea_dust')
    config.add_view('cta_project.views.wea_dust', route_name = 'wea_dust')	
	
    config.add_route('rec_temp', '/rec_temp')
    config.add_view('cta_project.views.rec_temp', route_name = 'rec_temp')	
	
    config.add_route('camtd_daq', '/camtd_daq')
    config.add_view('cta_project.views.camtd_daq', route_name = 'camtd_daq')
	
    config.add_route('camipr_daq', '/camipr_daq')
    config.add_view('cta_project.views.camipr_daq', route_name = 'camipr_daq')	
	
    config.add_route('camiprerr_daq', '/camiprerr_daq')
    config.add_view('cta_project.views.camiprerr_daq', route_name = 'camiprerr_daq')
	
    config.add_route('calq_cal', '/calq_cal')
    config.add_view('cta_project.views.calq_cal', route_name = 'calq_cal')
	
    config.add_route('calq_int', '/calq_int')
    config.add_view('cta_project.views.calq_int', route_name = 'calq_int')	
	
    config.add_route('calq_sig', '/calq_sig')
    config.add_view('cta_project.views.calq_sig', route_name = 'calq_sig')

    config.add_route('drvzd', '/drvzd')
    config.add_view('cta_project.views.drvzd', route_name = 'drvzd')
	
    config.add_route('drvdev_daq', '/drvdev_daq')
    config.add_view('cta_project.views.drvdev_daq', route_name = 'drvdev_daq')	
	
    config.add_route('camhv_daq', '/camhv_daq')
    config.add_view('cta_project.views.camhv_daq', route_name = 'camhv_daq')	
	
    config.add_route('camdc_daq', '/camdc_daq')
    config.add_view('cta_project.views.camdc_daq', route_name = 'camdc_daq')
	
    config.add_route('camdt_daq', '/camdt_daq')
    config.add_view('cta_project.views.camdt_daq', route_name = 'camdt_daq')	
	
    config.add_route('campd_daq', '/campd_daq')
    config.add_view('cta_project.views.campd_daq', route_name = 'campd_daq')
	
    config.add_route('campixtemp_daq', '/campixtemp_daq')
    config.add_view('cta_project.views.campixtemp_daq', route_name = 'campixtemp_daq')
	
    config.add_route('meanpixtemp_daq', '/meanpixtemp_daq')
    config.add_view('cta_project.views.meanpixtemp_daq', route_name = 'meanpixtemp_daq')	
	
    config.add_route('camclusttemp', '/camclusttemp')
    config.add_view('cta_project.views.camclusttemp', route_name = 'camclusttemp')

    config.add_route('camvcelbias_daq', '/camvcelbias_daq')
    config.add_view('cta_project.views.camvcelbias_daq', route_name = 'camvcelbias_daq')
	
    config.add_route('camlv1temp', '/camlv1temp')
    config.add_view('cta_project.views.camlv1temp', route_name = 'camlv1temp')	
	
    config.add_route('camlv2temp', '/camlv2temp')
    config.add_view('cta_project.views.camlv2temp', route_name = 'camlv2temp')	
	
    config.add_route('camlv1hum', '/camlv1hum')
    config.add_view('cta_project.views.camlv1hum', route_name = 'camlv1hum')
	
    config.add_route('camlv2hum', '/camlv2hum')
    config.add_view('cta_project.views.camlv2hum', route_name = 'camlv2hum')	
	
    config.add_route('camcoolfcptopleft', '/camcoolfcptopleft')
    config.add_view('cta_project.views.camcoolfcptopleft', route_name = 'camcoolfcptopleft')
	
    config.add_route('camcoolfcpbottright', '/camcoolfcpbottright')
    config.add_view('cta_project.views.camcoolfcpbottright', route_name = 'camcoolfcpbottright')
	
    config.add_route('camcoolrcptopleft', '/camcoolrcptopleft')
    config.add_view('cta_project.views.camcoolrcptopleft', route_name = 'camcoolrcptopleft')	
	
    config.add_route('camcoolrcpbottright', '/camcoolrcpbottright')
    config.add_view('cta_project.views.camcoolrcpbottright', route_name = 'camcoolrcpbottright')

    config.add_route('camcoolchasiastopleft', '/camcoolchasiastopleft')
    config.add_view('cta_project.views.camcoolchasiastopleft', route_name = 'camcoolchasiastopleft')
	
    config.add_route('camcoolchasiasbottright', '/camcoolchasiasbottright')
    config.add_view('cta_project.views.camcoolchasiasbottright', route_name = 'camcoolchasiasbottright')	
	
    config.add_route('camcoolchasiasftopleft', '/camcoolchasiasftopleft')
    config.add_view('cta_project.views.camcoolchasiasftopleft', route_name = 'camcoolchasiasftopleft')	
	
    config.add_route('camcoolchasiasfbottright', '/camcoolchasiasfbottright')
    config.add_view('cta_project.views.camcoolchasiasfbottright', route_name = 'camcoolchasiasfbottright')
	
    config.add_route('camcoolrearbottleft', '/camcoolrearbottleft')
    config.add_view('cta_project.views.camcoolrearbottleft', route_name = 'camcoolrearbottleft')	
	
    config.add_route('camcoolreartopleft', '/camcoolreartopleft')
    config.add_view('cta_project.views.camcoolreartopleft', route_name = 'camcoolreartopleft')
	
    config.add_route('camcoolfrontbottright', '/camcoolfrontbottright')
    config.add_view('cta_project.views.camcoolfrontbottright', route_name = 'camcoolfrontbottright')
	
    config.add_route('camcoolfronttopright', '/camcoolfronttopright')
    config.add_view('cta_project.views.camcoolfronttopright', route_name = 'camcoolfronttopright')	
	
    config.add_route('amcerr', '/amcerr')
    config.add_view('cta_project.views.amcerr', route_name = 'amcerr')

    config.add_route('l1t', '/l1t')
    config.add_view('cta_project.views.l1t', route_name = 'l1t')
	
    config.add_route('l2t', '/l2t')
    config.add_view('cta_project.views.l2t', route_name = 'l2t')	
	
    config.add_route('l2t_daq', '/l2t_daq')
    config.add_view('cta_project.views.l2t_daq', route_name = 'l2t_daq')	
	
    config.add_route('sumt_globr', '/sumt_globr')
    config.add_view('cta_project.views.sumt_globr', route_name = 'sumt_globr')
	
    config.add_route('sumt_l3', '/sumt_l3')
    config.add_view('cta_project.views.sumt_l3', route_name = 'sumt_l3')	
	
    config.add_route('sumt_dtw', '/sumt_dtw')
    config.add_view('cta_project.views.sumt_dtw', route_name = 'sumt_dtw')
	
    config.add_route('sumt_cbt1', '/sumt_cbt1')
    config.add_view('cta_project.views.sumt_cbt1', route_name = 'sumt_cbt1')
	
    config.add_route('sumt_cbt2', '/sumt_cbt2')
    config.add_view('cta_project.views.sumt_cbt2', route_name = 'sumt_cbt2')	
	
    config.add_route('sumt_ac', '/sumt_ac')
    config.add_view('cta_project.views.sumt_ac', route_name = 'sumt_ac')
	
    config.add_route('sumt_astrob', '/sumt_astrob')
    config.add_view('cta_project.views.sumt_astrob', route_name = 'sumt_astrob')
	
    config.add_route('cool_crate', '/cool_crate')
    config.add_view('cta_project.views.cool_crate', route_name = 'cool_crate')	
	
    config.add_route('cool_rack', '/cool_rack')
    config.add_view('cta_project.views.cool_rack', route_name = 'cool_rack')	
	
    config.add_route('calbtemp1', '/calbtemp1')
    config.add_view('cta_project.views.calbtemp1', route_name = 'calbtemp1')
	
    config.add_route('calbtemp2', '/calbtemp2')
    config.add_view('cta_project.views.calbtemp2', route_name = 'calbtemp2')	
	
    config.add_route('calbhum', '/calbhum')
    config.add_view('cta_project.views.calbhum', route_name = 'calbhum')
	
    config.add_route('sg_devaz', '/sg_devaz')
    config.add_view('cta_project.views.sg_devaz', route_name = 'sg_devaz')
	
    config.add_route('sg_devzd', '/sg_devzd')
    config.add_view('cta_project.views.sg_devzd', route_name = 'sg_devzd')	
	
    config.add_route('sg_camcx', '/sg_camcx')
    config.add_view('cta_project.views.sg_camcx', route_name = 'sg_camcx')

    config.add_route('sg_camcy', '/sg_camcy')
    config.add_view('cta_project.views.sg_camcy', route_name = 'sg_camcy')
	
    config.add_route('sg_stars', '/sg_stars')
    config.add_view('cta_project.views.sg_stars', route_name = 'sg_stars')	
	
    config.add_route('sg_bright', '/sg_bright')
    config.add_view('cta_project.views.sg_bright', route_name = 'sg_bright')	
	
    config.add_route('wea_temp', '/wea_temp')
    config.add_view('cta_project.views.wea_temp', route_name = 'wea_temp')
	
    config.add_route('pyro_cloud', '/pyro_cloud')
    config.add_view('cta_project.views.pyro_cloud', route_name = 'pyro_cloud')	
	
    config.add_route('pyro_skyt', '/pyro_skyt')
    config.add_view('cta_project.views.pyro_skyt', route_name = 'pyro_skyt')
	
    config.add_route('las_trans3km', '/las_trans3km')
    config.add_view('cta_project.views.las_trans3km', route_name = 'las_trans3km')
	
    config.add_route('las_trans6km', '/las_trans6km')
    config.add_view('cta_project.views.las_trans6km', route_name = 'las_trans6km')	
	
    config.add_route('las_trans9km', '/las_trans9km')
    config.add_view('cta_project.views.las_trans9km', route_name = 'las_trans9km')
	
    config.add_route('las_trans12km', '/las_trans12km')
    config.add_view('cta_project.views.las_trans12km', route_name = 'las_trans12km')
	
    config.add_route('muon_psf', '/muon_psf')
    config.add_view('cta_project.views.muon_psf', route_name = 'muon_psf')	
	
    config.add_route('muon_psfn', '/muon_psfn')
    config.add_view('cta_project.views.muon_psfn', route_name = 'muon_psfn')	
	
    config.add_route('muon_size', '/muon_size')
    config.add_view('cta_project.views.muon_size', route_name = 'muon_size')
	
    config.add_route('sbigpsf_b', '/sbigpsf_b')
    config.add_view('cta_project.views.sbigpsf_b', route_name = 'sbigpsf_b')	
	
    config.add_route('sbigpsf_l', '/sbigpsf_l')
    config.add_view('cta_project.views.sbigpsf_l', route_name = 'sbigpsf_l')
	
    config.add_route('bias_sig', '/bias_sig')
    config.add_view('cta_project.views.bias_sig', route_name = 'bias_sig')	
	
    config.add_route('hitfrac_sig', '/hitfrac_sig')
    config.add_view('cta_project.views.hitfrac_sig', route_name = 'hitfrac_sig')
	
    config.add_route('arrtm_cal', '/arrtm_cal')
    config.add_view('cta_project.views.arrtm_cal', route_name = 'arrtm_cal')	
	
    config.add_route('arrtm_int', '/arrtm_int')
    config.add_view('cta_project.views.arrtm_int', route_name = 'arrtm_int')
	
    config.add_route('arrtm_sig', '/arrtm_sig')
    config.add_view('cta_project.views.arrtm_sig', route_name = 'arrtm_sig')
	
    config.add_route('arrtmrms_cal', '/arrtmrms_cal')
    config.add_view('cta_project.views.arrtmrms_cal', route_name = 'arrtmrms_cal')	
	
    config.add_route('arrtmrms_int', '/arrtmrms_int')
    config.add_view('cta_project.views.arrtmrms_int', route_name = 'arrtmrms_int')
	
    config.add_route('arrtmrms_sig', '/arrtmrms_sig')
    config.add_view('cta_project.views.arrtmrms_sig', route_name = 'arrtmrms_sig')
	
    config.add_route('ped_ped', '/ped_ped')
    config.add_view('cta_project.views.ped_ped', route_name = 'ped_ped')	
	
    config.add_route('ped_int', '/ped_int')
    config.add_view('cta_project.views.ped_int', route_name = 'ped_int')	
	
    config.add_route('npe_int', '/npe_int')
    config.add_view('cta_project.views.npe_int', route_name = 'npe_int')
	
    config.add_route('pedrms_ped', '/pedrms_ped')
    config.add_view('cta_project.views.pedrms_ped', route_name = 'pedrms_ped')	
	
    config.add_route('pedrms_int', '/pedrms_int')
    config.add_view('cta_project.views.pedrms_int', route_name = 'pedrms_int')

    config.add_route('cfact_int', '/cfact_int')
    config.add_view('cta_project.views.cfact_int', route_name = 'cfact_int')
    config.add_route('wea_wsy', '/wea_wsy')	
    config.add_view('cta_project.views.wea_wsy', route_name = 'wea_wsy')
    config.add_route('wea_humy', '/wea_humy')
    config.add_view('cta_project.views.wea_humy', route_name = 'wea_humy')
    config.add_route('wea_gusty', '/wea_gusty')
    config.add_view('cta_project.views.wea_gusty', route_name = 'wea_gusty')
	
    config.add_route('wea_seey', '/wea_seey')
    config.add_view('cta_project.views.wea_seey', route_name = 'wea_seey')
	
    config.add_route('wea_dusty', '/wea_dusty')
    config.add_view('cta_project.views.wea_dusty', route_name = 'wea_dusty')	
	
    config.add_route('rec_tempy', '/rec_tempy')
    config.add_view('cta_project.views.rec_tempy', route_name = 'rec_tempy')	
	
    config.add_route('camtd_daqy', '/camtd_daqy')
    config.add_view('cta_project.views.camtd_daqy', route_name = 'camtd_daqy')
	
    config.add_route('camipr_daqy', '/camipr_daqy')
    config.add_view('cta_project.views.camipr_daqy', route_name = 'camipr_daqy')	
	
    config.add_route('camiprerr_daqy', '/camiprerr_daqy')
    config.add_view('cta_project.views.camiprerr_daqy', route_name = 'camiprerr_daqy')
	
    config.add_route('calq_caly', '/calq_caly')
    config.add_view('cta_project.views.calq_caly', route_name = 'calq_caly')
	
    config.add_route('calq_inty', '/calq_inty')
    config.add_view('cta_project.views.calq_inty', route_name = 'calq_inty')	
	
    config.add_route('calq_sigy', '/calq_sigy')
    config.add_view('cta_project.views.calq_sigy', route_name = 'calq_sigy')

    config.add_route('drvzdy', '/drvzdy')
    config.add_view('cta_project.views.drvzdy', route_name = 'drvzdy')
	
    config.add_route('drvdev_daqy', '/drvdev_daqy')
    config.add_view('cta_project.views.drvdev_daqy', route_name = 'drvdev_daqy')	
	
    config.add_route('camhv_daqy', '/camhv_daqy')
    config.add_view('cta_project.views.camhv_daqy', route_name = 'camhv_daqy')	
	
    config.add_route('camdc_daqy', '/camdc_daqy')
    config.add_view('cta_project.views.camdc_daqy', route_name = 'camdc_daqy')
	
    config.add_route('camdt_daqy', '/camdt_daqy')
    config.add_view('cta_project.views.camdt_daqy', route_name = 'camdt_daqy')	
	
    config.add_route('campd_daqy', '/campd_daqy')
    config.add_view('cta_project.views.campd_daqy', route_name = 'campd_daqy')
	
    config.add_route('campixtemp_daqy', '/campixtemp_daqy')
    config.add_view('cta_project.views.campixtemp_daqy', route_name = 'campixtemp_daqy')
	
    config.add_route('meanpixtemp_daqy', '/meanpixtemp_daqy')
    config.add_view('cta_project.views.meanpixtemp_daqy', route_name = 'meanpixtemp_daqy')	
	
    config.add_route('camclusttempy', '/camclusttempy')
    config.add_view('cta_project.views.camclusttempy', route_name = 'camclusttempy')

    config.add_route('camvcelbias_daqy', '/camvcelbias_daqy')
    config.add_view('cta_project.views.camvcelbias_daqy', route_name = 'camvcelbias_daqy')
	
    config.add_route('camlv1tempy', '/camlv1tempy')
    config.add_view('cta_project.views.camlv1tempy', route_name = 'camlv1tempy')	
	
    config.add_route('camlv2tempy', '/camlv2tempy')
    config.add_view('cta_project.views.camlv2tempy', route_name = 'camlv2tempy')	
	
    config.add_route('camlv1humy', '/camlv1humy')
    config.add_view('cta_project.views.camlv1humy', route_name = 'camlv1humy')
	
    config.add_route('camlv2humy', '/camlv2humy')
    config.add_view('cta_project.views.camlv2humy', route_name = 'camlv2humy')	
	
    config.add_route('camcoolfcptoplefty', '/camcoolfcptoplefty')
    config.add_view('cta_project.views.camcoolfcptoplefty', route_name = 'camcoolfcptoplefty')
	
    config.add_route('camcoolfcpbottrighty', '/camcoolfcpbottrighty')
    config.add_view('cta_project.views.camcoolfcpbottrighty', route_name = 'camcoolfcpbottrighty')
	
    config.add_route('camcoolrcptoplefty', '/camcoolrcptoplefty')
    config.add_view('cta_project.views.camcoolrcptoplefty', route_name = 'camcoolrcptoplefty')	
	
    config.add_route('camcoolrcpbottrighty', '/camcoolrcpbottrighty')
    config.add_view('cta_project.views.camcoolrcpbottrighty', route_name = 'camcoolrcpbottrighty')

    config.add_route('camcoolchasiastoplefty', '/camcoolchasiastoplefty')
    config.add_view('cta_project.views.camcoolchasiastoplefty', route_name = 'camcoolchasiastoplefty')
	
    config.add_route('camcoolchasiasbottrighty', '/camcoolchasiasbottrighty')
    config.add_view('cta_project.views.camcoolchasiasbottrighty', route_name = 'camcoolchasiasbottrighty')	
	
    config.add_route('camcoolchasiasftoplefty', '/camcoolchasiasftoplefty')
    config.add_view('cta_project.views.camcoolchasiasftoplefty', route_name = 'camcoolchasiasftoplefty')	
	
    config.add_route('camcoolchasiasfbottrighty', '/camcoolchasiasfbottrighty')
    config.add_view('cta_project.views.camcoolchasiasfbottrighty', route_name = 'camcoolchasiasfbottrighty')
	
    config.add_route('camcoolrearbottlefty', '/camcoolrearbottlefty')
    config.add_view('cta_project.views.camcoolrearbottlefty', route_name = 'camcoolrearbottlefty')	
	
    config.add_route('camcoolreartoplefty', '/camcoolreartoplefty')
    config.add_view('cta_project.views.camcoolreartoplefty', route_name = 'camcoolreartoplefty')
	
    config.add_route('camcoolfrontbottrighty', '/camcoolfrontbottrighty')
    config.add_view('cta_project.views.camcoolfrontbottrighty', route_name = 'camcoolfrontbottrighty')
	
    config.add_route('camcoolfronttoprighty', '/camcoolfronttoprighty')
    config.add_view('cta_project.views.camcoolfronttoprighty', route_name = 'camcoolfronttoprighty')	
	
    config.add_route('amcerry', '/amcerry')
    config.add_view('cta_project.views.amcerry', route_name = 'amcerry')

    config.add_route('l1ty', '/l1ty')
    config.add_view('cta_project.views.l1ty', route_name = 'l1ty')
	
    config.add_route('l2ty', '/l2ty')
    config.add_view('cta_project.views.l2ty', route_name = 'l2ty')	
	
    config.add_route('l2t_daqy', '/l2t_daqy')
    config.add_view('cta_project.views.l2t_daqy', route_name = 'l2t_daqy')	
	
    config.add_route('sumt_globry', '/sumt_globry')
    config.add_view('cta_project.views.sumt_globry', route_name = 'sumt_globry')
	
    config.add_route('sumt_l3y', '/sumt_l3y')
    config.add_view('cta_project.views.sumt_l3y', route_name = 'sumt_l3y')	
	
    config.add_route('sumt_dtwy', '/sumt_dtwy')
    config.add_view('cta_project.views.sumt_dtwy', route_name = 'sumt_dtwy')
	
    config.add_route('sumt_cbt1y', '/sumt_cbt1y')
    config.add_view('cta_project.views.sumt_cbt1y', route_name = 'sumt_cbt1y')
	
    config.add_route('sumt_cbt2y', '/sumt_cbt2y')
    config.add_view('cta_project.views.sumt_cbt2y', route_name = 'sumt_cbt2y')	
	
    config.add_route('sumt_acy', '/sumt_acy')
    config.add_view('cta_project.views.sumt_acy', route_name = 'sumt_acy')
	
    config.add_route('sumt_astroby', '/sumt_astroby')
    config.add_view('cta_project.views.sumt_astroby', route_name = 'sumt_astroby')
	
    config.add_route('cool_cratey', '/cool_cratey')
    config.add_view('cta_project.views.cool_cratey', route_name = 'cool_cratey')	
	
    config.add_route('cool_racky', '/cool_racky')
    config.add_view('cta_project.views.cool_racky', route_name = 'cool_racky')	
	
    config.add_route('calbtemp1y', '/calbtemp1y')
    config.add_view('cta_project.views.calbtemp1y', route_name = 'calbtemp1y')
	
    config.add_route('calbtemp2y', '/calbtemp2y')
    config.add_view('cta_project.views.calbtemp2y', route_name = 'calbtemp2y')	
	
    config.add_route('calbhumy', '/calbhumy')
    config.add_view('cta_project.views.calbhumy', route_name = 'calbhumy')
	
    config.add_route('sg_devazy', '/sg_devazy')
    config.add_view('cta_project.views.sg_devazy', route_name = 'sg_devazy')
	
    config.add_route('sg_devzdy', '/sg_devzdy')
    config.add_view('cta_project.views.sg_devzdy', route_name = 'sg_devzdy')	
	
    config.add_route('sg_camcxy', '/sg_camcxy')
    config.add_view('cta_project.views.sg_camcxy', route_name = 'sg_camcxy')

    config.add_route('sg_camcyy', '/sg_camcyy')
    config.add_view('cta_project.views.sg_camcyy', route_name = 'sg_camcyy')
	
    config.add_route('sg_starsy', '/sg_starsy')
    config.add_view('cta_project.views.sg_starsy', route_name = 'sg_starsy')	
	
    config.add_route('sg_brighty', '/sg_brighty')
    config.add_view('cta_project.views.sg_brighty', route_name = 'sg_brighty')	
	
    config.add_route('wea_tempy', '/wea_tempy')
    config.add_view('cta_project.views.wea_tempy', route_name = 'wea_tempy')
	
    config.add_route('pyro_cloudy', '/pyro_cloudy')
    config.add_view('cta_project.views.pyro_cloudy', route_name = 'pyro_cloudy')	
	
    config.add_route('pyro_skyty', '/pyro_skyty')
    config.add_view('cta_project.views.pyro_skyty', route_name = 'pyro_skyty')
	
    config.add_route('las_trans3kmy', '/las_trans3kmy')
    config.add_view('cta_project.views.las_trans3kmy', route_name = 'las_trans3kmy')
	
    config.add_route('las_trans6kmy', '/las_trans6kmy')
    config.add_view('cta_project.views.las_trans6kmy', route_name = 'las_trans6kmy')	
	
    config.add_route('las_trans9kmy', '/las_trans9kmy')
    config.add_view('cta_project.views.las_trans9kmy', route_name = 'las_trans9kmy')
	
    config.add_route('las_trans12kmy', '/las_trans12kmy')
    config.add_view('cta_project.views.las_trans12kmy', route_name = 'las_trans12kmy')
	
    config.add_route('muon_psfy', '/muon_psfy')
    config.add_view('cta_project.views.muon_psfy', route_name = 'muon_psfy')	
	
    config.add_route('muon_psfny', '/muon_psfny')
    config.add_view('cta_project.views.muon_psfny', route_name = 'muon_psfny')	
	
    config.add_route('muon_sizey', '/muon_sizey')
    config.add_view('cta_project.views.muon_sizey', route_name = 'muon_sizey')
	
    config.add_route('sbigpsf_by', '/sbigpsf_by')
    config.add_view('cta_project.views.sbigpsf_by', route_name = 'sbigpsf_by')	
	
    config.add_route('sbigpsf_ly', '/sbigpsf_ly')
    config.add_view('cta_project.views.sbigpsf_ly', route_name = 'sbigpsf_ly')
	
    config.add_route('bias_sigy', '/bias_sigy')
    config.add_view('cta_project.views.bias_sigy', route_name = 'bias_sigy')	
	
    config.add_route('hitfrac_sigy', '/hitfrac_sigy')
    config.add_view('cta_project.views.hitfrac_sigy', route_name = 'hitfrac_sigy')
	
    config.add_route('arrtm_caly', '/arrtm_caly')
    config.add_view('cta_project.views.arrtm_caly', route_name = 'arrtm_caly')	
	
    config.add_route('arrtm_inty', '/arrtm_inty')
    config.add_view('cta_project.views.arrtm_inty', route_name = 'arrtm_inty')
	
    config.add_route('arrtm_sigy', '/arrtm_sigy')
    config.add_view('cta_project.views.arrtm_sigy', route_name = 'arrtm_sigy')
	
    config.add_route('arrtmrms_caly', '/arrtmrms_caly')
    config.add_view('cta_project.views.arrtmrms_caly', route_name = 'arrtmrms_caly')	
	
    config.add_route('arrtmrms_inty', '/arrtmrms_inty')
    config.add_view('cta_project.views.arrtmrms_inty', route_name = 'arrtmrms_inty')
	
    config.add_route('arrtmrms_sigy', '/arrtmrms_sigy')
    config.add_view('cta_project.views.arrtmrms_sigy', route_name = 'arrtmrms_sigy')
	
    config.add_route('ped_pedy', '/ped_pedy')
    config.add_view('cta_project.views.ped_pedy', route_name = 'ped_pedy')	
	
    config.add_route('ped_inty', '/ped_inty')
    config.add_view('cta_project.views.ped_inty', route_name = 'ped_inty')	
	
    config.add_route('npe_inty', '/npe_inty')
    config.add_view('cta_project.views.npe_inty', route_name = 'npe_inty')
	
    config.add_route('pedrms_pedy', '/pedrms_pedy')
    config.add_view('cta_project.views.pedrms_pedy', route_name = 'pedrms_pedy')	
	
    config.add_route('pedrms_inty', '/pedrms_inty')
    config.add_view('cta_project.views.pedrms_inty', route_name = 'pedrms_inty')

    config.add_route('cfact_inty', '/cfact_inty')
    config.add_view('cta_project.views.cfact_inty', route_name = 'cfact_inty')		
    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.MongoClient
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.MongoClient):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan('cta_project')
    return config.make_wsgi_app()
	
