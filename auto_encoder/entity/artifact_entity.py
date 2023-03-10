from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    merge_df_path:str

@dataclass
class DataCleaningArtifact:
    pass

@dataclass
class DataValidationArtifact:
    pass

@dataclass
class DataTransformationArtifact:
    pass

@dataclass
class ModelTrainerArtifact:
    pass

@dataclass
class ModelEvaluationArtifact:
    pass

@dataclass
class ModelpusherArtifact:
    pass