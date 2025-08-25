{

    'name':'mi nuevo modulo',
    'author': 'unla',
    'version':'1.0.0',
    "description": "test",

    'depends': ['base'],
    'data': [
       
        'security/real_estate_res_groups.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/real_estate_menuitems.xml'
        
        
        ] ,
        
    "installable": True,
    'application': True



}