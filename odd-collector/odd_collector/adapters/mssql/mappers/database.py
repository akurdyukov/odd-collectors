from odd_models.models import DataEntity, DataEntityGroup, DataEntityType
from oddrn_generator import MssqlGenerator


def map_database(
    name: str,
    group_oddrns: list[str],
    oddrn_generator: MssqlGenerator,
) -> DataEntity:
    return DataEntity(
        type=DataEntityType.DATABASE_SERVICE,
        name=name,
        owner=None,
        oddrn=oddrn_generator.get_oddrn_by_path("databases", name),
        data_entity_group=DataEntityGroup(entities_list=group_oddrns),
    )
