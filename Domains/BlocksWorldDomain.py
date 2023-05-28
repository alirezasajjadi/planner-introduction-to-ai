from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate


class BlocksWorldDomain(Domain):
    def __init__(self):
        # Initialize name, object types and actions for the domain
        self.name = "BlocksWorld Domain"
        self.object_type = {"Blocks": [], "table": ["table1"]}
        self.actions = []

        # Define the possible objects in the domain (tires and locations)
        self.define_objects()
        # Define the available actions in the domain
        self.define_actions()

    def define_objects(self):
        # Add two types of tires and two locations to the domain
        self.object_type["Blocks"].append("A")
        self.object_type["Blocks"].append("B")
        self.object_type["Blocks"].append("C")
        self.object_type["Blocks"].append("D")

    def define_actions(self):

        for block in self.object_type["Blocks"]:
            clear_block = Predicate(
                "Clear",
                [block]
            )
            on_table = Predicate(
                "OnTable",
                [block, "table1"]
            )
            for from_location in self.object_type["Blocks"]:
                if block != from_location:
                    block_on_from_location = Predicate(
                        "On",
                        [block, from_location]
                    )
                    clear_from_location = Predicate(
                        "Clear",
                        [from_location]
                    )
                    move_from_table = f"Move({block},table1,{from_location})"
                    move_action = Action(
                        move_from_table,
                        [on_table, clear_block, clear_from_location],
                        [],
                        [block_on_from_location],
                        [on_table, clear_from_location]
                    )
                    self.actions.append(move_action)

                    move_to_table = f"MoveToTable({block},{from_location})"
                    # print(move_to_table)
                    MoveToTable = Action(
                        move_to_table,
                        [block_on_from_location, clear_block],
                        [],
                        [on_table, clear_from_location],
                        [block_on_from_location]
                    )
                    self.actions.append(MoveToTable)

                    for to_location in self.object_type["Blocks"]:
                        if block != to_location and from_location != to_location:

                            clear_to_location = Predicate(
                                "Clear",
                                [to_location]
                            )

                            block_on_to_location = Predicate(
                                "On",
                                [block, to_location]
                            )
                            # print(f"block: {block}, from_loc: {from_location}, to_loc: {to_location}")

                            # define move action
                            move = f"Move({block},{from_location},{to_location})"
                            # print(move)
                            move_action = Action(
                                move,
                                [block_on_from_location, clear_block, clear_to_location],
                                [],
                                [block_on_to_location, clear_from_location],
                                [block_on_from_location, clear_to_location]
                            )
                            self.actions.append(move_action)
