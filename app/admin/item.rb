ActiveAdmin.register Item do
  index do
        column :id
        column :name
        column :visits
        column :hierarchy
        column :description
        default_actions
    end
end
