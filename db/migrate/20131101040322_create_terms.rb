class CreateTerms < ActiveRecord::Migration
  def change
    create_table :terms do |t|
      t.string :data
      t.integer :id_item

      t.timestamps
    end
  end
end
