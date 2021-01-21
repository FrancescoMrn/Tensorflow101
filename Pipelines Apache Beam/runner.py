import os
import sklearn
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# parameters configuration
_pipeline_name = "wine_quality_processing"
_project_root = os.getcwd() 
_data_root = os.path.join(_project_root, "Pipelines Apache Beam/data", "winequality-red.csv")
_outputdir = os.path.join(_project_root, "Pipelines Apache Beam/data", "winequality-red_processed.csv")

encoding_dictionary = {"1":"0", "2":"0", "3":"0", "4":"1", "5":"1", "6":"2", "7":"2", "8":"3", "9":"3","10":"4"}

class LabelEncoder(beam.DoFn):
  #override process function
  def process(self, row):
    label = row[11]
    label_encoded = [label.replace(label, encoding_dictionary[label])]
    return [row + label_encoded]

with beam.Pipeline(options=PipelineOptions()) as pipeline:

    input_collection = (
      pipeline
      | "Reading csv" >> beam.io.ReadFromText(_data_root, skip_header_lines=1)
      | "Splitting records" >> beam.Map(lambda x: x.split(','))
    )

    wine_quality_encoding = (
      input_collection
      | "Quality buckets" >> beam.ParDo(LabelEncoder())
    )

    output = (
      wine_quality_encoding
      | 'Write output' >> beam.io.WriteToText(_outputdir)
    )
   
