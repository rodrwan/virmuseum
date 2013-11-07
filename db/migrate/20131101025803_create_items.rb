class CreateItems < ActiveRecord::Migration
  def change
    create_table :items do |t|
      t.string :name
      t.string :cientific_name
      t.text :description
      t.integer :visits
      t.integer :visible
      
      t.timestamps
    end
  end
end
