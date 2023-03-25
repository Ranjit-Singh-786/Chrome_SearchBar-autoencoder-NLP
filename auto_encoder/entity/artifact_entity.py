from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    merge_df_path:str

@dataclass
class DataValidationArtifact:
    validation_report_file_path:str

@dataclass
class DataCleaningArtifact:
    cleaned_file_path:str



@dataclass
class DataTransformationArtifact:
    transformed_data_file_path:str
    lemmetized_data_file_path:str
    vocab_size:int
    x_train_data_path:str
    y_train_data_path:str
    word_index_path:str

@dataclass
class ModelTrainerArtifact:
    model_file_path:str
    epoch_history_file_path:str
    x_train_file_path:str
    y_train_file_path:str

@dataclass
class ModelEvaluationArtifact:
    pass

@dataclass
class ModelpusherArtifact:
    pass