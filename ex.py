import graphene
from graphene_django import DjangoObjectType
from graphene_gis.converter import gis_converter
from graphql_jwt.decorators import login_required
from graphene_django_extras import DjangoSerializerType
from graphene_django_extras.paginations import (
    PageGraphqlPagination,
    LimitOffsetGraphqlPagination
)
from cartesApp.models import ArchiveJoolProj, JoolProj, Parametres
from authApp.models import Utilisateur
from coreApp.models import MyCodeException
from volumeApp.models import OperationVolume, TypeOperationVolume
from .serializers import *


class StateModelType(DjangoSerializerType):
    class Meta:
        description = "State model"
        serializer_class = StateSerializer
        # exclude_fields = ('geom_geometrie', )
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "etiquette": ('exact',)
        }

class JoolProjParametresModelType(DjangoSerializerType):
    class Meta:
        description = "JoolProjParametres model"
        serializer_class = JoolProjParametresSerializer
        # exclude_fields = ('geom_geometrie', )
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "deleted": ('exact',),
            "joolproj": ('exact',),
            "joolproj__number_of_images": ('exact',),
            "joolproj__title": ('exact', 'contains', 'icontains',),
            "parametres__title": ('exact', 'contains', 'icontains',),
        }


class ParametresModelType(DjangoSerializerType):
    class Meta:
        description = "Parametres model"
        serializer_class = ParametresSerializer
        # exclude_fields = ('geom_geometrie', )
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "deleted": ('exact',),
            "defaut": ('exact',),
            "sup_cent": ('exact',),
            "title": ('exact', 'contains', 'icontains',),
        }


class ContoursModelType(DjangoSerializerType):
    class Meta:
        description = "Contours model"
        serializer_class = ContoursSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "link": ("exact",),
            "status": ("exact",),
            "jproj__id": ("exact",),
            "interval": ("exact",),
        }


class RapportModelType(DjangoSerializerType):
    class Meta:
        description = "Rapport model"
        serializer_class = RapportSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "state__etiquette": ("exact", "lt", "gt"),
            "joolproj__id": ("exact",),
            "deleted": ('exact',),
        }


class JoolProjModelType(DjangoSerializerType):
    class Meta:
        description = "JoolProj model"
        serializer_class = JoolProjSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        exclude_fields = ('files_jpg', 'files_tiff')
        filter_fields = {
            "id": ("exact",),
            "state__etiquette": ("exact", "lt", "gt"),
            "title": ("icontains", "in",),
            "created_at": ("lte", "gte",),
            "number_of_images": ("lte", "gte",),
            "deleted": ('exact',),
            "task_id_jpg": ("exact",),
            "task_id_tiff": ("exact",),
            "start_processing": ("exact",),
            "end_processing": ("exact",),
            "start_post_processing": ("exact",),
            "end_post_processing": ("exact",),
            "img_folder": ("exact",),
            "completed": ("exact",),
            "bound": ("icontains", "in",),
            "task_status": ("exact",),
            "polygone__id": ("exact",),
            "project__id": ("exact",),
            "polygone__acteur__id": ("exact",),
            "polygone__acteur__libelle": ("icontains", "in",),
            "polygone__acteur__created_at": ("lte", "gte",),
            "polygone__superficie": ("lte", "gte",),
        }


class JoolProjType(DjangoObjectType):
    class Meta:
        model = JoolProj
        exclude = ('files_jpg', 'files_tiff')


class DtmModelType(DjangoSerializerType):
    class Meta:
        description = "DTM model"
        serializer_class = DtmSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        exclude_fields = ('files_jpg', 'files_tiff')
        filter_fields = {
            "id": ("exact",),
            "jproj": ("exact",),
            "deleted": ('exact',),
        }


class DsmModelType(DjangoSerializerType):
    class Meta:
        description = "Dsm model"
        serializer_class = DsmSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        exclude_fields = ('files_jpg', 'files_tiff')
        filter_fields = {
            "id": ("exact",),
            "jproj": ("exact",),
            "deleted": ('exact',),
        }


class PartageModelType(DjangoSerializerType):
    class Meta:
        description = "Partage model"
        serializer_class = PartageSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "owner": ('exact',),
            "destinataire": ('exact',),
            "email": ('exact',),
            "is_validate": ('exact',),
            "deleted": ('exact',),
        }


class CartesPartageesModelType(DjangoSerializerType):
    class Meta:
        description = "CartesPartagees model"
        serializer_class = CartesPartageesSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "partage": ('exact',),
            "joolproj": ('exact',),
            "joolproj__polygone__acteur__id": ('exact',),
            "active": ('exact',),
            "deadline": ('exact', 'lte', 'gte'),
        }


class JoolProjTreeModelType(DjangoSerializerType):
    class Meta:
        description = "JoolProjTree model"
        serializer_class = JoolProjTreeSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-created_at")
        filter_fields = {
            "id": ("exact",),
            "joolproj": ('exact',),
            "deleted": ('exact',),
            "joolproj__polygone__acteur": ('exact',),
            "culture": ('exact',),
            "status": ('iexact',),
            "nb_trees": ('exact', 'lte', 'gte',),
            "nb_trees_manual": ('exact', 'lte', 'gte',),
            "tree_bound_manual": ('exact', 'lte', 'gte',),
            "trees_bound": ('exact', 'lte', 'gte',),
            "precision": ('exact',),
            "patch_size": ('exact',),
            "deleted": ('exact',),
        }





class Next_Step(graphene.Mutation):
    joolproj = graphene.Field(JoolProjType)

    class Arguments:
        id = graphene.UUID(required=True)

    def mutate(root, info, id):
        try:
            carto = JoolProj.objects.filter(id=id, deleted = False).first()
            if carto is not None:
                carto.next_step()
                return Next_Step(joolproj=carto)

        except Exception as e:
            print("Error Next_Step", e)

        
        
class Restarting(graphene.Mutation):
    joolproj = graphene.Field(JoolProjType)
    class Arguments:
        id = graphene.UUID(required=True)
        node_log_jpg = graphene.String(default_value = "")
        node_log_tiff = graphene.String(default_value = "")

    def mutate(root, info, id, node_log_jpg, node_log_tiff):
        try:
            carto = JoolProj.objects.filter(id=id, deleted = False).first()
            if carto is not None:
                carto.restarting(node_log_jpg, node_log_tiff)
                return Restarting(joolproj=carto)

        except Exception as e:
            print("Error Restarting", e)       
        
        
class Failed(graphene.Mutation):
    joolproj = graphene.Field(JoolProjType)
    class Arguments:
        id = graphene.UUID(required=True)

    def mutate(root, info, id):
        try:
            carto = JoolProj.objects.filter(id=id, deleted = False).first()
            if carto is not None:
                carto.failed()
                return Failed(joolproj=carto)

        except Exception as e:
            print("Error Failed", e)       


        
class RemakeJoolProj(graphene.Mutation):
    joolproj = graphene.Field(JoolProjType)

    class Arguments:
        joolproj = graphene.UUID(required=True)
        title = graphene.String(required=True)
        dtm_factice = graphene.Boolean(required=True)
        dsm_factice = graphene.Boolean(required=True)
        params_factice = graphene.UUID(required=True)

    def mutate(root, info, joolproj, title, dtm_factice, dsm_factice, params_factice):
        carto = JoolProj.objects.filter(id=joolproj).first()
        userr = Utilisateur.objects.get(user_ptr=info.context.user.id, deleted=False)

        if userr.enterprise != carto.utilisateur.enterprise:
            raise Exception(MyCodeException.ACCESS_DENIED)

        if carto is not None:
            ArchiveJoolProj.objects.create(
                joolproj=carto,
                files_jpg=carto.files_jpg,
                files_tiff=carto.files_tiff,
                parametres=Parametres.objects.get(id=carto.params_factice).options,
                number_of_images=carto.number_of_images,
                img_folder=carto.img_folder,
                dtm_factice=carto.dtm_factice,
                dsm_factice=carto.dsm_factice,
                assets_jpg=carto.assets_jpg,
                assets_tiff=carto.assets_tiff,
                task_processing_time=carto.task_processing_time,
                task_status=carto.task_status,
                node_log_jpg=carto.node_log_jpg,
                node_log_tiff=carto.node_log_tiff,
                utilisateur=userr
            )

            # Debit espace client
            try:
                type_operation = TypeOperationVolume.objects.get(etiquette="UPLOADED")
                OperationVolume.objects.create(
                    size=carto.images_size,
                    description="Traitement de la cartogaphie `{}` de {} images".format(title, str(carto.number_of_images)),
                    type_operation_volume=type_operation,
                    tag = carto.id,
                    utilisateur=carto.utilisateur
                )

                carto.id = None
                carto.title = title
                carto.task_status = "RUNNING"
                carto.dsm_factice = dsm_factice
                carto.dtm_factice = dtm_factice
                carto.params_factice = params_factice
                carto.assets_jpg = ""
                carto.img_folder = ""
                carto.task_id_jpg = ""
                carto.task_id_tiff = ""
                carto.task_processing_time = 0
                carto.task_progress = 0
                carto.nb_restart = 0
                carto.node_log_jpg = ""
                carto.node_log_tiff = ""
                carto.start_processing = False
                carto.end_processing = False
                carto.completed = False
                carto.bound = ""
                carto.utilisateur = userr

                carto.save()

                return RemakeJoolProj(joolproj=carto)

            except Exception as e:
                print("Error volume", e)

            return JoolProjModelType(carto)

        raise Exception(MyCodeException.ERROR)


class RestartJoolProj(graphene.Mutation):
    joolproj = graphene.Field(JoolProjType)

    class Arguments:
        joolproj = graphene.UUID(required=True)
        utilisateur = graphene.ID(required=True)

    def mutate(root, info, joolproj, utilisateur):
        carto = JoolProj.objects.filter(id=joolproj).first()
        print("-------------", joolproj, carto is None)
        if carto is not None:
            if carto.task_status == "FAILED":
                archive = ArchiveJoolProj.objects.create(
                    joolproj=carto,
                    files_jpg=carto.files_jpg,
                    files_tiff=carto.files_tiff,
                    parametres=Parametres.objects.get(id=carto.params_factice).options,
                    number_of_images=carto.number_of_images,
                    img_folder=carto.img_folder,
                    dtm_factice=carto.dtm_factice,
                    dsm_factice=carto.dsm_factice,
                    assets_jpg=carto.assets_jpg,
                    assets_tiff=carto.assets_tiff,
                    task_processing_time=carto.task_processing_time,
                    task_status=carto.task_status,
                    node_log_jpg=carto.node_log_jpg,
                    node_log_tiff=carto.node_log_tiff,
                    utilisateur=Utilisateur.objects.get(id=utilisateur)
                )

                carto.task_status = "RUNNING"
                carto.assets_jpg = ""
                carto.img_folder = ""
                carto.task_id_jpg = ""
                carto.task_id_tiff = ""
                carto.task_processing_time = 0
                carto.task_progress = 0
                carto.nb_restart = 0
                carto.node_log_jpg = ""
                carto.node_log_tiff = ""
                carto.start_processing = False
                carto.end_processing = False
                carto.completed = False
                carto.bound = ""
                carto.save()

                return RestartJoolProj(joolproj=carto)

            raise Exception(MyCodeException.ERROR)
        raise Exception(MyCodeException.ERROR)




class CartesAppMutation(object):
    # Dtm
    create_dtm = DtmModelType.CreateField()
    update_dtm = DtmModelType.UpdateField()

    # Dsm
    create_dsm = DsmModelType.CreateField()
    update_dsm = DsmModelType.UpdateField()

    # Contours
    create_contours = ContoursModelType.CreateField()
    update_contours = ContoursModelType.UpdateField()
    delete_contours = ContoursModelType.DeleteField()

    # JoolProj
    create_jool_proj        = JoolProjModelType.CreateField()
    update_jool_proj        = JoolProjModelType.UpdateField()
    restart_jool_proj       = RestartJoolProj.Field()
    remake_jool_proj        = RemakeJoolProj.Field()
    Next_Step_jool_proj     = Next_Step.Field()
    Failed_jool_proj        = Failed.Field()
    restarting_jool_proj    = Restarting.Field()

    # Parametres
    create_parametres = ParametresModelType.CreateField()
    update_parametres = ParametresModelType.UpdateField()

    # JoolProjParametres
    create_joolproj_parametres = JoolProjParametresModelType.CreateField()
    update_joolproj_parametres = JoolProjParametresModelType.UpdateField()

    # JoolProjParametres
    create_joolproj_parametres = JoolProjParametresModelType.CreateField()
    update_joolproj_parametres = JoolProjParametresModelType.UpdateField()

    # PartageModelType
    create_cartes_partagees = CartesPartageesModelType.CreateField()
    update_cartes_partagees = CartesPartageesModelType.UpdateField()

    # PartageModelType
    create_partage = PartageModelType.CreateField()
    update_partage = PartageModelType.UpdateField()

    # JoolProjTreeModelType
    create_jool_proj_tree = JoolProjTreeModelType.CreateField()
    update_jool_proj_tree = JoolProjTreeModelType.UpdateField()

    # RapportModelType
    create_rapport = RapportModelType.CreateField()
    update_rapport = RapportModelType.UpdateField()

