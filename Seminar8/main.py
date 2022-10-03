import user_interface as ui
import logger as lg
import  crud


lg.logging.info('Start')
crud.init_data_base('company_base.csv')
ui.show_menu()
