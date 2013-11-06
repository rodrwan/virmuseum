ActiveAdmin.register User do
    index do
        column :id
        column :name
        column "Role", :role
        default_actions
    end
end
