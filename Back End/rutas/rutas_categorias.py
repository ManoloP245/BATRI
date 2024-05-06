from flask import jsonify,request
from modelos.categorias import Categorias
from conexiondb.database import db_session

def rutas_categorias(app):

    @app.route('/consultar_categorias')
    def consultar_categorias():
        try:
            categorias = []
            sql = Categorias.query.all()
            for categoria in sql:
                datos_categoria = {
                    "id_categoria": categoria.id_categoria,
                    "nombre":categoria.nombre,
                    "descripcion":categoria.descripcion,
                    "estado":categoria.estado,
                }
                categorias.append(datos_categoria)
            json_data = jsonify(categorias)    
            return json_data 
        except:  
            return jsonify({"msg": "No se encontraron categorias","estado":False})     
        
    @app.route('/consultar_categoria/<id_categoria>')
    def consultar_categoria(id_categoria):
        try:
            categoria = Categorias.query.filter_by(id_categoria=id_categoria).first()
            datos_categoria = {
                    "id_categoria": categoria.id_categoria,
                    "nombre":categoria.nombre,
                    "descripcion":categoria.descripcion,
                    "estado":categoria.estado,
                }
            json_data = jsonify(datos_categoria)    
            return json_data
        except:    
            return jsonify({"msg": "No se encontro categoria","estado":False})
        
    @app.route("/crear_categoria",methods=["POST"])    
    def crear_categoria():
        datos = request.json
        nombre = datos.get('nombre')
        descripcion = datos.get('descripcion')
        estado = datos.get('estado')
        try:
            crear= Categorias(nombre, descripcion,estado)
            db_session.add(crear)
            db_session.commit()
            return jsonify({"msg": "Exito al crear el categoria","estado":True}) 
        except:    
            return jsonify({"msg": "No se pudo crear el categoria","estado":False})
        
    @app.route("/actualizar_categoria/<int:id_categoria>",methods=["PUT"]) 
    def actualizar_categoria(id_categoria):
        datos = request.json
        nombre = datos.get('nombre')
        descripcion = datos.get('descripcion')
        estado = datos.get('estado')
        try:
            categoria = Categorias.query.filter_by(id_categoria=id_categoria).first()
            if categoria:
                categoria.nombre = nombre
                categoria.descripcion = descripcion
                categoria.estado = estado
                db_session.commit()
                return jsonify({"msg": "Éxito al actualizar el categoria", "estado": True})
            else:
                return jsonify({"msg": "No se encontró el categoria", "estado": False})
        except Exception as e:    
            return jsonify({"msg": f"No se pudo actualizar el categoria: {str(e)}", "estado": False})
        
    @app.route("/eliminar_categoria/<int:id_categoria>",methods=["DELETE"]) 
    def eliminar_categoria(id_categoria):
        try:
            categoria = Categorias.query.get(id_categoria)
            if categoria:
                db_session.delete(categoria)
                db_session.commit()
                return jsonify({"msg": "categoria eliminado exitosamente", "estado": True})
            else:
                return jsonify({"msg": "No se encontró el categoria", "estado": False})
        except Exception as e:
            return jsonify({"msg": f"No se pudo eliminar el categoria: {str(e)}", "estado": False})