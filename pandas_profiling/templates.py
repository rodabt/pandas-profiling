# coding=UTF-8

'''This file contains all templates used for generating the HTML profile report'''

from jinja2 import Environment, PackageLoader
import os

# i18n suppport
import i18n
LOCALE = 'es'

i18n.load_path.append('pandas_profiling/locale')
i18n.set('locale', LOCALE)

# Initializing Jinja
pl = PackageLoader('pandas_profiling', 'templates')
jinja2_env = Environment(lstrip_blocks=True, trim_blocks=True, loader=pl)

# Define global translated html headers and text sections
html_text = dict()
file = os.path.join(os.path.dirname(__file__), 'locale/html.' + LOCALE + '.yml')
file_contents = ''
with open(file, 'r') as f:
    file_contents = f.read()

html = [s.split(":")[0].strip() for s in file_contents.split("\n")]
text = [s for s in html if s][1:]
for s in text:
    html_text[s] = i18n.t('html.' + s)

# Make html_text accesible to all templates
jinja2_env.globals['html_text'] = html_text

# Mapping between template name and file
templates = {'freq_table_row': 'freq_table_row.html',
             'mini_freq_table_row': 'mini_freq_table_row.html',
             'freq_table': 'freq_table.html',
             'mini_freq_table': 'mini_freq_table.html',
             'row_num': 'row_num.html',
             'row_date': 'row_date.html',
             'row_cat': 'row_cat.html',
             'row_corr': 'row_corr.html',
             'row_const': 'row_const.html',
             'row_unique': 'row_unique.html',
             'overview': 'overview.html',
             'sample': 'sample.html',
             'base': 'base.html',
             'wrapper': 'wrapper.html'
             }

# Mapping between row type and var type
var_type = {'NUM': i18n.t('templates.num'),
            'DATE': i18n.t('templates.date'),
            'CAT': i18n.t('templates.cat'),
            'UNIQUE': i18n.t('templates.uniq'),
            'CONST': i18n.t('templates.const'),
            'CORR': i18n.t('templates.corr')
            }


def template(template_name):
    """Return a jinja template ready for rendering. If needed, global variables are initialized.

    Parameters
    ----------
    template_name: str, the name of the template as defined in the templates mapping

    Returns
    -------
    The Jinja template ready for rendering
    """
    globals = None
    if template_name.startswith('row_'):
        # This is a row template setting global variable
        globals = dict()
        globals['vartype'] = var_type[template_name.split('_')[1].upper()]
    return jinja2_env.get_template(templates[template_name], globals=globals)


# mapping between row type and template name
row_templates_dict = {'NUM': template('row_num'),
                      'DATE': template('row_date'),
                      'DISCRETE': template('row_num'),
                      'CAT': template('row_cat'),
                      'UNIQUE': template('row_unique'),
                      'CONST': template('row_const'),
                      'CORR': template('row_corr')
                      }

messages = dict()
messages['CONST'] = u'{0[varname]}' + i18n.t('templates._has_constant_value_') + '{0[mode]}' + ' <span class="label label-primary">' + i18n.t('templates.Rejected') + '</span>'
messages['CORR'] = u'{0[varname]}' + i18n.t('templates._is_highly_correlated_with_') + '{0[correlation_var]} (ρ = {0[correlation]}) <span class="label label-primary">' + i18n.t('templates.Rejected') + '</span>'
messages['HIGH_CARDINALITY'] = u'{varname}' + i18n.t('templates._has_a_high_cardinality_') + ': {0[distinct_count]}' + i18n.t('templates._distinct_values_') +  '<span class="label label-warning">' + i18n.t('templates.Warning') + '</span>'
messages['n_duplicates'] = u''+ i18n.t('templates.Dataset_has_') + '{0[n_duplicates]}' + i18n.t('templates._duplicate_rows_') + '<span class="label label-warning">' + i18n.t('templates.Warning') + '</span>'
messages['skewness'] = u'{varname}' + i18n.t('templates._is_highly_skewed_') + '(γ1 = {0[skewness]})'
messages['p_missing'] = u'{varname}' + i18n.t('templates._has_') + '{0[n_missing]} / {0[p_missing]}' + i18n.t('templates._missing_values_') + '<span class="label label-default">' + i18n.t('templates.Missing') + '</span>'
messages['p_infinite'] = u'{varname}' + i18n.t('templates._has_') + '{0[n_infinite]} / {0[p_infinite]}' + i18n.t('templates._infinite_values_') + '<span class="label label-default">' + i18n.t('templates.Infinite') + '</span>'
messages['p_zeros'] = u'{varname}' + i18n.t('templates._has_') + '{0[n_zeros]} / {0[p_zeros]}' + i18n.t('templates._zeros')

message_row = u'<li>{message}</l>'