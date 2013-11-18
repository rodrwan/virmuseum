class CreateDataStreams < ActiveRecord::Migration
  def change
    create_table :data_streams do |t|
      t.string :url
      t.string :data_type

      t.timestamps
    end
  end
end
