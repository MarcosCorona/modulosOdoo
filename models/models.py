# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

#Comentario
from odoo import models ,fields, api

class departamento(models.Model):
	_name = 'proyectos.departamento'
	_description = 'Define los atributos de un departamento'

	#atributos
	nombreDpto = fields.Char(string='Nombre departamento', required=True)

class empleado(models.Model):
	_name = 'proyectos.empleado'
	_description = 'Define los atributos de un empleado'
	 
	#atributos
	dniEmpleado = fields.Char(string = 'Dni ',required = True)
	nombreEmpleado = fields.Char(string = 'Nombre ',required = True)
	fechaNacimiento = fields.Date(string = 'Fecha Nacimiento',required = True, default = fields.Date.today())
	direccionEmpleado = fields.Char(string = 'Direccion ',required = True)
	telefonoEmpleado = fields.Char(string = 'Telefono ',required = True)

class proyecto(models.Model):
	_name = 'proyectos.proyecto'
	_description = 'Define los atributos de un proyecto'

	#atributos
	nombreProyecto = fields.Char(string = 'Nombre proyecto',required = True)
	tipoProyecto = fields.Selection(string = 'Tipo proyecto',selection =[('f','Front-End'),('b','Back-end')],help='Tipo de proyecto al que est� destinado')
	ciudadProyecto = fields.Char(string='Ciudad',required = True)
	descripcionProyecto = fields.Text(string ='Descripcion proyecto',required = True)

	