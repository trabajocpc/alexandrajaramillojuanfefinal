import pandas as pd
from data.platos import platosPopulares
from data.creartabla import creartabla

from data.reservas import reservas
from data.provedores import proveedores

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
creartabla(tablaPlatos,"tablaplatospopulares")

tablaReservas=pd.DataFrame(reservas)
print(tablaReservas)
creartabla(tablaReservas,"tablaReservas")

tablaproveedores=pd.DataFrame(proveedores)
print(tablaproveedores)
creartabla(tablaproveedores,"tablaproveedores")