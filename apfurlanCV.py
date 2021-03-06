# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import streamlit as st
import numpy as np
from PIL import Image
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
#from pycaret.classification import load_model, predict_model
  
#st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.header('**Alexandre Furlan**') 
st.sidebar.write('*physics , mathematics, data science, machine learning and trading*') 

st.sidebar.write(' :mailbox_closed:   Email : ')
st.sidebar.write('alexandrepfurlan@gmail.com')

linkhp = '[www.apfurlan.com](http://www.apfurlan.com)'
st.sidebar.write(':earth_americas:  Homepage : ')
st.sidebar.markdown(linkhp,unsafe_allow_html=True)


linkgh = '[https://github.com/apfurlan](https://github.com/apfurlan)'
st.sidebar.write(' Github : ')
st.sidebar.markdown(linkgh,unsafe_allow_html=True)


linkld = '[https://linkedin.com/apfurlan](https://www.linkedin.com/in/alexandre-furlan-b69251120/)'
st.sidebar.write(' LinkedIn : ')
st.sidebar.markdown(linkld,unsafe_allow_html=True)


img = Image.open("euSusto.jpeg") 
  
# display image using streamlit 
# width is used to set the width of an image 
st.image(img, width=150, heigth=150) 

#st.markdown('(https://github.com/apfurlan/StreamlitCV/euSusto.jpeg)')

#st.markdown('![alt text](https://raw.githubusercontent.com/ricardorocha86/StreamlitCV/main/Imagem8.png)')
sections = ['About me',
          'Education',
          'Publications',
          'Conferences',
          'Data Science',
          'Trading and Stock Markets']


col = st.beta_columns(len(sections)) 
names = []
for i in range(len(sections)): names.append(i)
for i in range(len(sections)): names[i] = col[i].button(sections[i])


###### PRESENTATION ######
if names[0]  :
    	
    st.write("""
	I studied physics at [Universidade Federal do Paraná](https://https://fisica.ufpr.br/) (Curitiba-PR).
    Earned my M.Sc and Ph.D degrees from [Universidade Federal do Rio Grande do Sul](https://www.if.ufrgs.br/if/)
    (Porto Alegre-RS)  through the study of the influence of the disorder and solutes in the anomalous 
    behavior of the liquid state. This work was performed under the supervision of Marcia Barbosa and 
    Carlos Fiore. with a doctoral collaborative period at Statistical Mechanics and Condensed Matter 
    Group of the Institute of Physical Chemistry Rocasolano (Madrid-Spain) under the supervision of 
    Enrique Lomba and Noé Almarza. \
    
    I'm currently postdoc at the Physics Department of the 
    [Universidade Federal de Minas Gerais](https://www.fisica.ufmg.br/) 
    (Belo Horizonte-MG-Brazil), working with Ronald Dickman, on the study of the disorder 
    effects in the critical behavior of different lattice gases and also in the Entropic Sampling 
    Monte Carlo Simulations.
	""")
    
elif names[1] :     
    st.write("""
        2005-2010 - B.Sc. in Physics, Department of Physics, Universidade Federal do Paraná   
        **Advisor :** Carlos Eduardo Fiore dos Santos   
        **Project :** Phase transitions and criticality on simplified statistical models.   

       ----      
    
       2011-2013 - M.Sc. in Physics, Physics Institute, Universidade Federal do Rio Grande do Sul   
      **Advisor :** Marcia Cristina Bernardes Barbosa   
      **Project :** Effects of confinement in porous matrix on the anomalous properties 
      of water-like systems.     

    ----   

    2013-2017 - Doctoral degree in Science, Physics Institute, Universidade Federal do 
    Rio Grande do Sul           
    **Advisor :** Marcia Cristina Bernardes Barbosa       
    **Project :** Cofinement and mixtures in water-like models.       
    **Collaboration :** From 01/2016 to 08/2016 I studied at the goup Institute of Physical 
    Chemistry "Rocasolano"at Consejo Superior de Investigaciones Científicas - CSIC.
             """)
elif names[3] : 
    st.write("""
     1. Encontro Nacional de Física. “Temperature of maximum density and excess properties of a simple model of short-chain alcohol aqueous solution”, Natal - RN - 2016.


    2. STATPHYS 26. “Lattice Model for water-solute mixtures”, Lyon - France - 2016.


    3. VI Workshop in Complexity of Water and Other Liquids. “Influence of disordered porous media in the anomalous properties of a associative lattice gas”. - Araranguá - SC - Brazil - 2016.


    4.  Encontro Nacional de Física Estatística. “Influence of disordered porous media in the anomalous properties of a simple water model” - Vitória - ES - Brazil - 2015.

    5. V Workshop in Complexity of Water and Other Liquids. “Influence of disordered porous media in the anomalous properties of a associative lattice gas”. - Araranguá- SC - Brazil - 2014.


    6. IV Workshop in Complexity of Water and Other Liquids. “Lattice model for water-methanol interaction”. - Araranguá - SC - Brazil - 2013.

    7. Summer school - Laboratório Nacional de Computação Científica. 2012.

    8. Workshop on "Structure and Dynamics of Glassy, Supercooled and Nanoconfined Fluids". “Thermodynamic and dynamics anomalies in water in porous media”. Buenos Aires - Argentina - 2012.

    9. EVINCI (Evento de iniciação cientiífica) - “Phase transitions and criticality on simplified statistical models” - 2010 - Curitiba - PR -Brazil.

    10. 14th Summer School Universidade de São Paulo - São Paulo - Brazil 2010.

    11. Summer school : Laboratório Associado de Computação e Matemática Aplicada(Laboratory for computing and applied mathematics) - LAC - INPE. - São José dos Campos - SP - Brazil 2010.
            
    12. Summer School : Mathematics - Universidade Federal do Paraná - 2009.

    13. Simpósio Nacional de Ensino de Física. 2007. (Simposium).
            
   14. Summer School : Mathematics - Universidade Federal do Paraná - 2009.
                  
             """)

elif names[2] : 
    st.write("""
    1. **A. P. Furlan**, Diogo C. dos Santos, Robert M. Ziff, and Ronald Dickman, 
    *Jamming and percolation of dimers in restricted-valence random sequential adsorption* - 
    [Phys. Rev. Research 2, 043027 (2020)]   
    
    2.  **A. P. Furlan**, Tiago J. Oliveira, Jürgen F. Stilck, and Ronald Dickman, 
    *Order-disorder transition in a two-dimensional associating lattice gas* - 
    [Phys. Rev. E 100, 022109 (2019)]   
    
    3. **A. P. Furlan**, E. Lomba, M. C. Barbosa , *Temperature of maximum density and excess properties of short-chain alcohol aqueous solutions: A simplified model simulation study* - [J. Chem. Phys. 146 144503 (2017)] , [arXiv:1701.08670]

    4. L. Pinheiro, **A. P. Furlan**, L.B. Krott, A. Diehl and M.C. Barbosa , *Critical points, phase transitions and water-like anomalies for an isotropic two length scale potential with increasing attractive well* - [Physica A 468 866 (2017)] - [arXiv:1607.02941]

    5. **A. P. Furlan**, N. G. Almarza, M. C. Barbosa , *Lattice model for water-solute mixtures* - [J. Chem. Phys. 145 144501 (2016)] - [arXiv:1605.05228]

    6. **A. P. Furlan**, Carlos E. Fiore, M. C. Barbosa , *Influence of disordered porous 
    media on the anomalous properties of a simple water model* - [Phys. Rev. E 92 032404 (2015)] - [arXiv:1504.04608]   
    
    ----   
    
    **In progress :**
    
     * **A. P. Furlan**, I.  Ibagon, Ronald  Dickman, 
    *Critical lines and universality in the 2D symmetric associating lattice gas* - [In preparation]
    
     * I. Ibagon, **A. P. Furlan**, Ronald  Dickman, 
    *Contact process in fragmented environments* - [In preparation]   
    
    *  **A. P. Furlan**, Diogo C. dos Santos, Robert M. Ziff, and Ronald Dickman,  
    *Random sequential adsorption of oriented dimers with vertex restrictions* - [In preparation]
    
     """)
elif names[4] : 
    st.write("""
             # Data Science      
            """)
    
elif names[5] : 
    st.write("""
             # Trading and Stock Markets   
             """)

else :
     st.write("""
	I studied physics at [Universidade Federal do Paraná](https://https://fisica.ufpr.br/) (Curitiba-PR).
    Earned my M.Sc and Ph.D degrees from [Universidade Federal do Rio Grande do Sul](https://www.if.ufrgs.br/if/)
    (Porto Alegre-RS)  through the study of the influence of the disorder and solutes in the anomalous 
    behavior of the liquid state. This work was performed under the supervision of Marcia Barbosa and 
    Carlos Fiore. with a doctoral collaborative period at Statistical Mechanics and Condensed Matter 
    Group of the Institute of Physical Chemistry Rocasolano (Madrid-Spain) under the supervision of 
    Enrique Lomba and Noé Almarza. \
    
    I'm currently postdoc at the Physics Department of the 
    [Universidade Federal de Minas Gerais](https://www.fisica.ufmg.br/) 
    (Belo Horizonte-MG-Brazil), working with Ronald Dickman, on the study of the disorder 
    effects in the critical behavior of different lattice gases and also in the Entropic Sampling 
    Monte Carlo Simulations.
	""")    


    
st.sidebar.markdown('---')  
st.sidebar.markdown('---')  
st.sidebar.markdown(':copyright: Alexandre Furlan') 
#st.sidebar.markdown('---')