class CreateTerms < ActiveRecord::Migration
  def change
    create_table :terms do |t|
      t.string :data
      t.integer :count
      
      t.timestamps
    end
  end
end
