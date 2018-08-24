import collections

# quantities
quantities = collections.OrderedDict([
    ('density', dict(label='Density', range=[10.0,1200.0], unit='kg/m^3')),
    ('deliverable_capacity', dict(label='Deliverable capacity', range=[0.0,300.0], default=[175,300], unit='v STP/v')),
    ('absolute_methane_uptake_high_P', dict(label='CH4 uptake High-P', range=[0.0,200.0], unit='mol/kg')),
    ('absolute_methane_uptake_low_P', dict(label='CH4 uptake Low-P', range=[0.0,200.0], unit='mol/kg')),
    ('heat_desorption_high_P', dict(label='CH4 heat of desorption High-P', range=[0.0,30.0], unit='kJ/mol')),
    ('heat_desorption_low_P', dict(label='CH4 heat of desorption Low-P', range=[0.0,30.0], unit='kJ/mol')),    
    ('supercell_volume', dict(label='Supercell volume', range=[0.0,1000000.0], unit='A^3')),
    ('surface_area', dict(label='Geometric surface area', range=[0.0,12000.0], unit='m^2/g')),
])

bondtype_dict = collections.OrderedDict([
    ('amide', "#1f77b4"), ('amine', "#d62728"), ('imine', "#ff7f0e"),
    ('CC', "#2ca02c"), ('mixed', "#778899"),
])


presets = {
    'default': { 
            'x': 'density',
            'y': 'deliverable_capacity',
          },
    '3a': { 'structure_filter': '2d',
            'x': 'density',
            'y': 'surface_area',
            'clr': 'bondtype',
          },
    '3b': { 'structure_filter': '3d',
            'x': 'density',
            'y': 'surface_area',
            'clr': 'bondtype',
          },
# x should be "delta heat of desorption
#    '6b': { 
#            'x': 'delta_heat_desorption',
#            'y': 'heat_desorption_low_P',
#            'clr': 'bondtype',
#          },
#    '6b': { 
#            'x': 'delta_heat_desorption',
#            'y': 'deliverable_capacity',
#            'clr': 'bondtype',
#          },
    '7a': { 
            'x': 'density',
            'y': 'absolute_methane_uptake_low_P',
            'clr': 'bondtype',
          },
    '7b': { 
            'x': 'density',
            'y': 'absolute_methane_uptake_high_P',
            'clr': 'bondtype',
          },
    '8b': { 'structure_filter': '2d',
            'x': 'density',
            'y': 'deliverable_capacity',
            'clr': 'bondtype',
          },
    '9b': { 'structure_filter': '3d',
            'x': 'density',
            'y': 'deliverable_capacity',
            'clr': 'bondtype',
          },
    '10b': { 
            'x': 'largest_included_sphere',
            'y': 'deliverable_capacity',
            'clr': 'bondtype',
          },
    '11': { 
            'x': 'surface_area',
            'y': 'deliverable_capacity',
            'clr': 'bondtype',
          },
    '12a': { 'bond_filter': 'amide',
            'x': 'density',
            'y': 'deliverable_capacity',
            'clr': 'topology',
          },
    '12b': { 'bond_filter': 'amine',
            'x': 'density',
            'y': 'deliverable_capacity',
            'clr': 'topology',
          },
    '12c': { 'bond_filter': 'imine',
            'x': 'density',
            'y': 'deliverable_capacity',
            'clr': 'topology',
          },
    '12d': { 'bond_filter': 'amide',
            'x': 'density',
            'y': 'deliverable_capacity',
            'clr': 'topology',
          },
}