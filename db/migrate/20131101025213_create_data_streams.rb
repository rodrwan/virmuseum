class CreateDataStreams < ActiveRecord::Migration
  def change
    create_table :data_streams do |t|
      t.integer :id_item
      t.integer :id_role
      t.string :info
      t.string :type_data

      t.timestamps
    end
  end
end
