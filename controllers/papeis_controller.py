from fastapi import APIRouter,Response
import ormar
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from models.papel import Papel
from models.requests.papel_update import PapelUpdate

router = APIRouter()



@router.get('/')
async def list_item():
    return await Papel.objects.all()

@router.post('/')
async def add_item(papel:Papel):
    await papel.save()
    return papel

@router.get('/{papel_id}')
@entidade_nao_encontrada
async def get_papel(papel_id:int):
    papel = await Papel.objects.get(id=papel_id)
    return papel

@router.patch('/{papel_id}')
@entidade_nao_encontrada
async def patch_papel(propriedades_atualizacao: PapelUpdate ,papel_id:int):
    papel_salvo = await Papel.objects.get(id=papel_id)
    propriedades_atualizacao = propriedades_atualizacao.dict(exclude_unset=True)
    await papel_salvo.update (**propriedades_atualizacao)
    return papel_salvo
    
@router.delete('/{papel_id}')
@entidade_nao_encontrada
async def delete_papel(papel_id:int):
    papel = await Papel.objects.get(id=papel_id)
    await papel.delete()
    return papel